from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    '''
    Base model for various models
    '''
    class Meta:
        abstract = True
