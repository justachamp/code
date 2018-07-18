from django.forms import ModelForm
from ui.storage.models import Audience


class AudienceForm(ModelForm):
    class Meta:
        model = Audience
        fields = ('name', 'owner')
        error_messages = {
            'name': {
                'required': 'Please, provide a name',
            }
        }
