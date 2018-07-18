import logging as log
import random
import string
from time import mktime
from datetime import datetime
from dirtyfields import DirtyFieldsMixin

from django.db import models as m, transaction
from django.dispatch import receiver
from django.db.utils import IntegrityError
from django.db.models.signals import pre_save

from adserving.bidder.spendings import delimit
from etc.constants import EPOCH, ID_RANDOM_LENGTH, PUBLIC_ID_DELIMITER


url_safe_chars = string.digits + string.ascii_letters


def public_id_randomizer():
    ''' Return random string of length equal to `ID_RANDOM_LENGTH`. '''
    choices = random.sample(url_safe_chars, ID_RANDOM_LENGTH)
    return ''.join(choices)


class RandomId(m.Model):

    id_random = m.CharField(max_length=128, unique=True)

    class Meta:
        abstract = True
        select_on_save = True

    @property
    def public_id_parts(self):
        return (self.id_random, )

    @property
    def public_id(self):
        return delimit(*self.public_id_parts)

    def _set_unique_field(self, tries=3, fieldname='id_random', rand_algorithm=public_id_randomizer):
        '''
        Attempt to generate and save unique self.id_random
        :param int tries: to generate unique id_random field (> 0)
        :param str fieldname: field to generate random value for
        :param function rand_algorithm: function to call to generate random value for field
        '''
        if getattr(self, fieldname):
            return

        id_rand = None

        # make sure we do not overwrite existing id with new one
        if self.pk:
            checked_data = self.__class__.objects.values(
                fieldname
            ).get(pk=self.pk)
            if checked_data and fieldname in checked_data:
                id_rand = checked_data[fieldname]

        if not id_rand:

            # Try to generate unique `id_random` field
            for i in range(tries):
                id_rand = rand_algorithm()
                if not self.__class__.objects.filter(
                        **{fieldname: id_rand}
                ).exists():
                    break
            else:
                error = "Could not produce unique {field} for {model} model.".format(
                    model=type(self),
                    field=fieldname)
                raise IntegrityError(error)

        setattr(self, fieldname, id_rand)

    @classmethod
    def objects_by_public_ids(cls, obj_list):
        '''
        gets objects based on public_id
        public_id may be:
            1. campaign - acc_hash(delimiter)camp_hash
            2. strategy - acc_hash(delimiter)camp_hash(delimiter)strategy_hash
            3. ad - acc_hash(delimiter)camp_hash(delimiter)strategy_hash(delimiter)ad_hash
        extracts public_id for given model ([-1]) and returns queryset
        filtered by this list.
        '''
        ids_random = [i.split(PUBLIC_ID_DELIMITER)[-1] for i in obj_list]
        return cls.objects.filter(id_random__in=ids_random)

    @classmethod
    def exists_by_public_id(cls, public_id):
        """
        Check if object with given public_id exists in database.
        """
        id_random = public_id.split(PUBLIC_ID_DELIMITER)[-1]
        return cls.objects.filter(id_random=id_random).exists()

    @transaction.atomic
    def save(self, tries=3, *args, **kwargs):
        ''' Attempt to generate and save unique self.id_random
        :param int tries: to generate unique id_random field (> 0)
        '''

        self._set_unique_field(tries)

        super(RandomId, self).save(*args, **kwargs)


class LatestUpdate(m.Model):

    object_name = m.CharField(max_length=255, unique=True)
    latest_update = m.DateTimeField(default=EPOCH)

    def __unicode__(self):
        return '%s / last_update %s' % (self.object_name, self.latest_update)

    @property
    def to_secs(self):
        '''
        :returns: datetime casted to int - seconds since the epoch
        :rtype: int
        '''
        return int(mktime(self.latest_update.timetuple()))

    @classmethod
    def by_name(cls, obj_name):
        obj, _ = cls.objects.get_or_create(object_name=obj_name)
        return obj

    def __enter__(self):
        ''' context manager that returns last update of object and saves now()
        as new 'latest_update' time.
        '''
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.save()  # update latest_update to now()


@receiver(pre_save, weak=False)
def latest_pre_save(sender, instance, **kwargs):

    if instance.pk:
        instance.latest_update = datetime.utcnow()


class NotRemovableManager(m.Manager):

    def delete(self, *args, **kwargs):
        raise IntegrityError(
            'These objects can not be deleted through Manager'
        )


class VisibleManager(NotRemovableManager):

    def get_query_set(self):
        return super(self.__class__, self).get_query_set() \
            .filter(is_deleted=False)


class NotRemovable(m.Model):

    ''' The Base class for models that should never be removed from db
    but should be only marked as deleted '''

    is_deleted = m.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True

    # default manager (returns all objects also removed from UI by user)
    objects = NotRemovableManager()
    # objects that are not visible in UI (removed by user)
    objects_visible = VisibleManager()

    def delete(self, force=False, *args, **kwargs):
        if force:
            cls = self.__class__
            log.warning("%s objects shouldn't be removed" % cls)
            super(cls, self).delete(*args, **kwargs)

        self.is_deleted = True
        self.save()


class KanaryDirtyFieldsMixin(DirtyFieldsMixin):

    """
    Extended DirtyFieldsMixin implementation with foreign key tracking.

    Also tracks related field changes.
    """

    def __init__(self, *args, **kwargs):
        super(KanaryDirtyFieldsMixin, self).__init__(*args, **kwargs)
        self._original_read_state = self._as_dict()

    def _as_dict(self):
        """
        Return model's field value as dict.

        .. note::

            In contrary to original implementation, instead leaving out foreign keys relation,
            uses their *field_id* form
        """
        field_names = [(f.name if not f.rel else f.name + '_id') for f in self._meta.concrete_fields]
        return {field_name: getattr(self, field_name) for field_name in field_names}

    def has_changed(self, fieldname, since_read=False):
        """
        Check if the fieldname has changed.

        :param str fieldname: field name
        :param bool since_read: whether to check against first read state (useful in post_save) or against recent save.

        :return: whether or not given field has changed
        :rtype: bool
        """
        fieldvalue = self._original_read_state[fieldname] if since_read else self._original_state[fieldname]
        return fieldvalue != getattr(self, fieldname)
