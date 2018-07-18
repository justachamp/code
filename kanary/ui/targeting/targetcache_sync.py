from itertools import chain
import ast

from django.db import connection

from etc import dimensions
from ui.targeting.targetcache import TargetCache
from ui.targeting.models import (
    TargetValue, TargetMap, ContentCategoryValue,
    Peer39BrandProtection,
    Peer39ContextualSegment,
    Peer39PageLanguage,
    Peer39PageQuality,
    SegmentProximicContextual,
    SegmentProximicMaturityRating,
    SegmentProximicPageLanguage,
    SegmentProximicPageNoticeability,
    SegmentProximicPagePlacement,
    SegmentProximicPageQuality,
    SegmentProximicSafetyLevel,
)


class TargetCacheSync(TargetCache):
    '''
    Utility to populate and drop redis targeting cache. May break when schema is altered
    because it uses raw SQL. The use of raw SQL is justified by memory and query count
    savings.
    '''

    class SQL(object):
        # Raw SQL makes it possible to use pure cursor API which works really
        # fast for large collections, unlike Django, which cannot manage memory
        # and blocks the system, even when using QuerySet.iterator.
        tv_ptv = '''SELECT exchange, category, value, id, category
            FROM {table} ORDER BY category;
        '''.format(table=TargetValue._meta.db_table)

        # Extensive use of raw SQL. Saves lots of queries.
        # Still heavy as hell.
        publisher_info = '''
SELECT id AS represented_pk,  /* Select all represented. */
       publisher_info._sizes,
       publisher_info._positions AS _positions,
       publisher_info.segments AS segments
FROM   targeting_targetvalue
       JOIN (SELECT targetvalue_ptr_id,  /* Join them with publisher_info. */
                    _sizes,
                    _positions,
                    ptvs_segments.segments AS segments
             FROM   targeting_publishertargetvalue
                    JOIN targeting_targetvalue AS tv
                      ON targetvalue_ptr_id = tv.id
                    JOIN (SELECT publishertargetvalue_id,  /* Compose segments by array-aggregating m2m relation. */
                                 Array_agg(appnexussegment_id) AS segments
                          FROM   targeting_publishertargetvalue_segments
                          GROUP  BY publishertargetvalue_id) AS ptvs_segments
                      ON targeting_publishertargetvalue.targetvalue_ptr_id =
                         ptvs_segments.publishertargetvalue_id
             WHERE  tv.category = 'publisher'
                    AND tv.representant_id IS NULL) AS publisher_info
         ON publisher_info.targetvalue_ptr_id = representant_id
WHERE  representant_id IS NOT NULL  /* Filter only represented. */
       AND representant_id != id;
'''

    @classmethod
    def populate(cls):
        '''
        Populate L2 targeting cache by traversing collections of data in postgres
        and putting that data to redis under keys formed by queries that match ones
        made by BidDimensionExtractor.

        Takes ~2 mins (for one million TargetValues and PublisherTargetValues as they
        are the greatest factor).
        '''
        cls.populate_tv_ptv()
        cls.populate_publisher_info()
        cls.populate_content_category()
        cls.populate_segments()

    @staticmethod
    def query_iter(sql):
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor

    @classmethod
    def populate_tv_ptv(cls):
        for exchange, category, value, pk, category in cls.query_iter(cls.SQL.tv_ptv):
            if exchange is None:
                continue
            value_list = TargetMap.unpack(value)

            if category == dimensions.g_publisher:
                # Mirroring query:
                # ui.targeting.models.PublisherTargetValueManager.get_or_create_multi_pk
                cls.set('publisher_value', exchange, value_list, pk)
            else:
                # Mirroring query:
                # ui.targeting.models.TargetValueManager.get_or_create_multi_pk
                cls.set('target_value', exchange, category, value_list, pk)

    @classmethod
    def populate_publisher_info(cls):
        for represented_pk, sizes, positions, segments in cls.query_iter(cls.SQL.publisher_info):
            publisher_info = {
                'sizes': ast.literal_eval(sizes),  # Sizes and positions are lists literals in strings.
                'positions': ast.literal_eval(positions),
                # Segments are array-aggregated by Postgres and mapped to a Python list.
                'segments': segments
            }
            cls.set('publisher_pk', represented_pk, publisher_info)

    @classmethod
    def populate_content_category(cls):
        # We can use Django ORM for ContentCategoryValue because there are ~500 of them
        # and that number is not going to increase drastically.
        for cc_value in ContentCategoryValue.objects.all():
            cls.set('content_category', cc_value.exchange, cc_value.name, cc_value.pk)

    @classmethod
    def populate_segments(cls):
        # Same for segments.
        for seg in chain(
                *[
                    m.objects.all() for m in
                    Peer39BrandProtection,
                    Peer39ContextualSegment,
                    Peer39PageLanguage,
                    Peer39PageQuality,
                    SegmentProximicContextual,
                    SegmentProximicMaturityRating,
                    SegmentProximicPageLanguage,
                    SegmentProximicPageNoticeability,
                    SegmentProximicPagePlacement,
                    SegmentProximicPageQuality,
                    SegmentProximicSafetyLevel,
                ]):
            cls.set('segment', 'appnexus', seg.DIMENSION, seg.appnexus_id, seg.pk)

    @classmethod
    def drop(cls):
        '''
        Flushes redis cache. All keys get flushed so make sure you don't use that
        db for another purpose.

        FLUSHDB is used, so other databases are safe.
        Takes almost no time.
        '''
        cls.tv_cache.client.clear()
