from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.db.models import Sum
from django.contrib.admin.views.main import ChangeList
from django.contrib.admin import DateFieldListFilter
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .models import (
    Invoice,
    Payment,
    User,
    Account
)

from ui.bidding_spendings.models import DailySpendings

admin.site.register(Invoice)
admin.site.register(Payment)


class UserInline(admin.TabularInline):
    model = User
    fields = ('username', 'email', 'login_link', 'edit')
    readonly_fields = fields
    actions = None
    max_num = 0
    extra = 0

    def edit(self, instance):
        url = reverse('admin:%s_%s_change'
                      % (instance._meta.app_label, instance._meta.module_name),
                      args=[instance.pk]
                      )
        return mark_safe(u'<a href="{u}">Edit</a>'.format(u=url))

    def login_link(self, instance):
        url = reverse('loginas-user-login', args=[instance.pk])
        return mark_safe(u'<a href="{u}">Login as user</a>'.format(u=url))

    def has_delete_permission(self, request, obj=None):
        return False


class DailySpendingsInline(admin.TabularInline):
    model = DailySpendings
    fields = (
        'date', 'budget_spent', 'hidden_commission', 'kanary_commission'
    )
    readonly_fields = fields

    actions = None
    max_num = 0
    extra = 0
    can_delete = False

    def has_delete_permission(self, request, obj=None):
        return False


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'commission')
    list_editable = ('commission',)
    search_fields = ('name',)
    fields = ('name', 'commission', 'timezone')
    readonly_fields = ('timezone',)
    inlines = [
        UserInline,
        DailySpendingsInline,
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Account, AccountAdmin)


class UserAdmin(admin.ModelAdmin):
    change_form_template = 'loginas/change_form.html'
    list_display = ('username', 'email', 'account_details')
    list_editable = ()
    fields = ('username', 'email', 'account', 'account_details')
    readonly_fields = ('account_details', )
    actions = None

    def account_details(self, instance):
        account = instance.account
        url = reverse('admin:%s_%s_change'
                      % (account._meta.app_label, account._meta.module_name),
                      args=[account.pk]
                      )
        return mark_safe(
            u'<a href="{u}">{n}</a>'.format(u=url, n=account.name)
        )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(User, UserAdmin)


class DailySpendingsList(ChangeList):

    fields_to_total = (
        'budget_spent', 'hidden_commission', 'kanary_commission',
        'data_cost_proximic', 'data_cost_peer39', 'data_cost_lotame'
    )

    def get_total_values(self, queryset):
        """
        Get the totals
        """
        total = DailySpendings()

        for field in self.fields_to_total:
            setattr(total, field, queryset.aggregate(Sum(field)).items()[0][1])

        return total

    def get_results(self, request):
        """
        The model admin gets queryset results from this method
        and then displays it in the template
        """
        super(DailySpendingsList, self).get_results(request)
        total = self.get_total_values(self.queryset)

        # small hack. in order to get the objects loaded we need to call for
        # queryset results once so simple len function does it
        len(self.result_list)

        # and finally we add our custom rows to the resulting changelist
        self.result_list._result_cache.insert(0, total)


class DateFieldListFilterSpendings(DateFieldListFilter):

    def __init__(self, field, request, params, model, model_admin, field_path):
        super(DateFieldListFilterSpendings, self).__init__(
            field, request, params, model, model_admin, field_path)

        now = timezone.now()
        if timezone.is_aware(now):
            now = timezone.localtime(now)

        today = now.date()

        if today.month == 1:
            prev_month = today.replace(year=today.year - 1, month=12, day=1)
        else:
            prev_month = today.replace(month=today.month - 1, day=1)

        if today.month <= 3:
            prev_three_month = today.replace(
                year=today.year - 1, month=12 - (3 - today.month), day=1
            )
        else:
            prev_three_month = today.replace(month=today.month - 3, day=1)

        self.links = list(self.links)

        self.links.insert(
            4,
            (_('Last month'), {
                self.lookup_kwarg_since: str(prev_month),
                self.lookup_kwarg_until: str(today.replace(day=1)),
            })
        )

        self.links.insert(
            5,
            (_('Last three months'), {
                self.lookup_kwarg_since: str(prev_three_month),
                self.lookup_kwarg_until: str(today.replace(day=1)),
            })
        )


class DailySpendingsAdmin(admin.ModelAdmin):
    fields = [
        'account',
        'date',
        '_budget_spent',
        '_hidden_commission',
        '_kanary_commission',
        '_audit_fees',
        '_data_cost_proximic',
        '_data_cost_peer39',
        '_data_cost_lotame',
    ]

    readonly_fields = fields
    list_display = fields

    list_filter = (
        'account',
        ('date', DateFieldListFilterSpendings),
    )

    actions = None
    can_delete = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_changelist(self, request, **kwargs):
        return DailySpendingsList

    @staticmethod
    def map_to_string(field):
        return "{0:.2f}".format(field or 0)

    def _budget_spent(self, obj):
        return self.map_to_string(obj.budget_spent)

    def _hidden_commission(self, obj):
        return self.map_to_string(obj.hidden_commission)

    def _kanary_commission(self, obj):
        return self.map_to_string(obj.kanary_commission)

    def _audit_fees(self, obj):
        return self.map_to_string(obj.audit_fees)

    def _data_cost_proximic(self, obj):
        return self.map_to_string(obj.data_cost_proximic)

    def _data_cost_peer39(self, obj):
        return self.map_to_string(obj.data_cost_peer39)

    def _data_cost_lotame(self, obj):
        return self.map_to_string(obj.data_cost_lotame)


admin.site.register(DailySpendings, DailySpendingsAdmin)
