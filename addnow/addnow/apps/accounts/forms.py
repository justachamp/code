from django import forms

from addnow.apps.accounts.models import User


class CreateSiteForm(forms.Form):

    url = forms.URLField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your website URL',
                                      'class': 'form-control'})
    )


class DSPPixelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('dsp_pixel_url', )
