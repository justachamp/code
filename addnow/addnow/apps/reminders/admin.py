from django.contrib import admin
from django.contrib.admin import register
from django.forms import ModelForm, TextInput, Textarea

from post_office.admin import EmailTemplateAdmin
from post_office.models import EmailTemplate
from suit.widgets import AutosizedTextarea

from addnow.apps.reminders.models import ReminderRule, ReminderLog


@register(ReminderRule)
class ReminderRuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'email_template', 'dimension', 'is_active']
    save_as = True


@register(ReminderLog)
class ReminderLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'rule', 'created_at']


class EmailTemplateForm(ModelForm):
    class Meta:
        widgets = {
            'description': AutosizedTextarea(attrs={'style': 'width: 99%'}),
            'subject': TextInput(attrs={'class': 'input-xlarge'}),
            'content': Textarea(attrs={'style': 'width: 99%'}),
            'html_content': Textarea(attrs={'rows': 30, 'style': 'width: 99%'})
        }


class EmailTemplateAdmin(EmailTemplateAdmin):
    form = EmailTemplateForm


admin.site.unregister(EmailTemplate)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
