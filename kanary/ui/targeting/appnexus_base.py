# AppNexus-specific targeting models

from django.db import models as m
from django.db import transaction, DatabaseError

from adserving.bidder.appnexus_api import api
from ui.targeting.utils import subclasses_of
from txmisc import log


class AppNexusBase(m.Model):

    # iterable of dicts {id:, name:, last_modified: ,...}
    api_method = NotImplemented
    dimension = None

    appnexus_id = m.IntegerField(unique=True)
    name = m.CharField(max_length=511)
    last_modified = m.DateTimeField(null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '{0} {1}'.format(self.appnexus_id, self.name)

    @staticmethod
    def _related_field(field, appnexus_id):
        rel_model = field.rel.to
        column = field.column
        pk = None
        try:
            fobj = rel_model.objects.get(appnexus_id=appnexus_id)
            pk = fobj.pk
        except rel_model.DoesNotExist:
            print 'There is no {0} with appnexus_id={1}' \
                .format(rel_model, appnexus_id)
        return column, pk

    @classmethod
    @transaction.atomic
    def update(cls):
        '''
        Calls cls.api_method, iterates over returned elements and
        updates them in database.
        cls.api_method should return iterable.
        '''

        for count, item in enumerate(cls.api_method(api)):
            if count % 10 == 0:
                print '.',
            try:
                obj = cls.objects.get(appnexus_id=item['id'])
            except cls.DoesNotExist:
                obj = cls(appnexus_id=item['id'])

            obj.name = item['name']
            obj.last_modified = item.get('last_modified')

            for field in cls._meta.fields:
                fname = field.name
                val = item.get(fname)
                if not val or fname == 'id':
                    continue

                # foreign key
                if field.rel:
                    fname, val = cls._related_field(field, val)

                setattr(obj, fname, val)

            obj.save()


class AppNexusTargetValue(m.Model):

    class Meta:
        abstract = True

    @property
    def translated_target_value(self):
        '''
        :returns: iterable that will be used to create/read
            translated target value
        :rtype: list
        '''
        return [self.name]

    @property
    def raw_target_value(self):
        '''
        :returns: iterable that will be used to create/read
            raw target value
        :rtype: list
        '''
        return [unicode(self.appnexus_id)]

    @classmethod
    @transaction.atomic
    def update_targetvalues(cls):
        '''
        Updates/Creates TargetValues for given AppnexusApiService object
        '''
        # circular
        from ui.targeting.models import TargetValue, TargetValueQueryError

        for obj in cls.objects.all():
            translated_target_value = obj.translated_target_value

            # if nothing gets returned, just continue
            if not translated_target_value:
                continue

            # Representant creation does not imply assigning representant
            # to unrepresented TargetValues.
            autotranslated_tv, created = TargetValue.objects \
                .get_or_create_representant(
                    category=cls.dimension,
                    value=translated_target_value,
                    strict=False)

            # if we read value from API and it's stored as represented it is
            # certainly a mistake on our side.
            # We can safely transform it to representing values
            # as represented are only numbers here
            if not created and\
                    not autotranslated_tv.is_representant and\
                    not autotranslated_tv.has_representant:
                autotranslated_tv.make_representant()
                autotranslated_tv.save()

            # We can create exchange-specific TargetValues from here.
            try:
                untranslated_tv, created = TargetValue.objects.\
                    get_or_create_unrepresented(
                        exchange='appnexus',
                        value=obj.raw_target_value,
                        category=obj.dimension,
                        strict=False
                    )
            except TargetValueQueryError:
                continue

            if not untranslated_tv.is_representant or not untranslated_tv.represented.exists():
                untranslated_tv.make_represented(autotranslated_tv)
                untranslated_tv.save()


def appnexus_targeting_update():
    '''Updates AppNexus targeting classes containing mapping of AppNexus
            IDs into verbose names'''

    for appnex_cls in subclasses_of(AppNexusBase, 'ui.targeting.appnexus'):
        print 'updating', appnex_cls, '...'

        try:
            appnex_cls.update()
        except DatabaseError, e:
            log.error('[appnexus_update_base:DatabaseError:%s] %r', (appnex_cls, e))
        print '\n'

    for appnex_cls in subclasses_of(AppNexusTargetValue,
                                    'ui.targeting.appnexus'):
        print 'updating target_values', appnex_cls, '...'

        try:
            appnex_cls.update_targetvalues()
        except DatabaseError, e:
            log.error('[appnexus_update_tg:DatabaseError:%s] %r', (appnex_cls, e))
        print '\n'
