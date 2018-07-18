import re
from operator import itemgetter
from adserving.types import is_real_number
from django.forms import ValidationError, ModelForm
from tastypie.validation import Validation
from ui.campaign.models import Campaign, Strategy


def validate_unique_name(form, model, error_text):
    '''
    Takes name passed to the form and checks if given model has an object
    already saved in database with the same name value.
    If yes returns validation error, if no returns passed name.
    '''
    name = form.cleaned_data['name']
    already_exists = model.objects.filter(name=name).exists()

    # when object is updating
    if form.instance.pk:
        old = model.objects.get(pk=form.instance.pk)
        if old.name == name:
            return name
        elif already_exists:
            raise ValidationError(error_text)

    # when object is creating
    elif already_exists:
        raise ValidationError(error_text)

    return name


class CampaignForm(ModelForm):

    class Meta:
        exclude = ('slug', 'id_random', 'budget_spent_commission', 'budget_spent')
        model = Campaign


class StrategyForm(ModelForm):

    class Meta:
        exclude = (
            'slug', 'campaign', 'landing_sites', 'type', 'id_random',
            'publisherset', 'targetingIncludeAudiences',
            'budget_spent_commission', 'budget_spent', 'targetingExcludeAudiences'
        )
        model = Strategy

    # Cleaning total budget is done in strategy_pre_save

    def clean_budget_daily(self, *args, **kwargs):
        budget_total = self.cleaned_data['budget_total']
        budget_daily = self.cleaned_data['budget_daily']
        if budget_total < budget_daily:
            raise ValidationError(
                'Daily strategy budget cannot be higher' +
                ' than total strategy budget.'
            )

        return budget_daily

    def clean_is_automatically_bidded(self, *args, **kwargs):
        '''
        This field enables/disable bid price optimizer.

        If optimizer is enabled, one of optimized metrics has to be chosen.
        Otherwise a default bid price has to be specified.
        '''
        is_automatically_bidded = self.cleaned_data['is_automatically_bidded']
        optimized_metric = self.cleaned_data['optimized_metric']
        bid = self.cleaned_data['budget_bid_CPM']

        if (is_automatically_bidded and optimized_metric is None):
            raise ValidationError(
                'Choose metric to optimize with automatic bid price'
            )

        if (not is_automatically_bidded and (not is_real_number(bid) or bid < 0)):
            raise ValidationError(
                'Default CPM bid is required and must be a nonnegative number'
            )


class StrategyValidation(Validation):

    def __init__(self, **kwargs):
        search_mappings = kwargs['search_mappings']
        self.searchFields = self.extract_pairs(search_mappings)

        super(StrategyValidation, self).__init__()

    def extract_pairs(self, mappings):
        pairs = {}
        for mapping in mappings:
            bundle, field = mapping
            category = self.extract_category(field)
            if category not in pairs:
                pairs[category] = [bundle]
            else:
                pairs[category].append(bundle)

        return pairs

    def extract_category(self, field):
        '''
            Extracts category name from field name
            :param str field {category}_include or {category}_exclude
        '''
        category = re.sub('_include', '', field)
        category = re.sub('_exclude', '', category)
        if not category:
            msg = "Field name doesn't match required format {category}_include or {category}_exclude"
            raise Exception(msg)
        return category

    def has_duplicates(self, includes, excludes, getIds):
        if getIds:
            mapper = itemgetter('id')
            includes = map(mapper, includes)
            excludes = map(mapper, excludes)
        repeated = (set(includes)).intersection(set(excludes))
        return len(repeated) > 0

    def check_duplicates(self, bundle, fields, byIds=False):
        errors = {}
        for category in fields:
            include = fields[category][0]
            exclude = fields[category][1]
            has_duplicates = self.has_duplicates(
                bundle.data[include],
                bundle.data[exclude],
                byIds
            )
            if has_duplicates:
                errors[category] = u"Cannot include and exlude the same values"
        return errors

    def check_advert_custom_trackers(self, bundle):
        """
        Validate custom trackers for adverts

        #. One advert can't have both trackers
        #. Custom JS tracker is not allowed for video creative

        :returns: dict with fields as keys and error messages as values
        :rtype dict
        """
        errors = {}
        for advert in bundle.data['adverts']:
            if advert['custom_pixel'] and advert['js_code']:
                errors['adverts'] = 'Cannot add both pixel and JS code tracker.'
            if advert['js_code'] and advert['creative_type'] == 'Video':
                errors['adverts_video'] = 'Cannot add JS tracker to video creative.'
        return errors

    def is_wrong_creative_destination(self, strategy_type, creative_destination):
        """ Return True if wrong destination.

            Available destinations:

            For type 'Web', 'Mobile':
                creative destination 'default'

            For type 'Facebook':
                creative destinations 'facebook_sidebar' and 'facebook_newsfeed'

            :rtype True or False
        """
        available_destinations = {
            'Web': ['default'],
            'Mobile': ['default'],
            'Facebook': ['facebook_sidebar', 'facebook_newsfeed'],
        }

        return (creative_destination not in available_destinations[strategy_type])

    def check_advert_creative_destination(self, bundle):
        """
        Validate creative destination in adverts.

        Strategy with 'Facebook' type should have facebook creatives.
        Strategy with 'Web' or 'Mobile' type should have default creatives.

        :returns: dict with fields as keys and error messages as values
        :rtype dict
        """
        errors = {}

        strategy_type = bundle.data['type']
        for creative in bundle.data['adverts']:
            creative_destination = creative['creative_destination']
            if self.is_wrong_creative_destination(strategy_type, creative_destination):
                errors['adverts'] = 'Cannot use %s creatives in strategy of %s type.' % (
                    creative_destination.replace('_', ' '),
                    strategy_type
                )
                return errors

        return errors

    def check_landing_sites_amount(self, bundle):
        """
        Validate strategy landing sites amount.
        For a facebook strategy should be only one landing site.

        :returns: dict with fields as keys and error messages as values
        :rtype dict
        """
        errors = {}
        landing_sites_amount = len(bundle.data['landing_sites'])
        if bundle.data['type'] == 'Facebook' and landing_sites_amount > 1:
            errors['landing'] = 'Facebook strategy can have only one landing page.'

        return errors

    def check_fb_creative_duplicates(self, bundle):
        """
        Check that facebook strategy does not have duplicate creatives.

        :returns: dict with fields as keys and error messages as values
        :rtype dict
        """
        errors = {}
        if bundle.data['type'] == 'Facebook':
            creative_ids = []
            for creative in bundle.data['adverts']:
                c_id = creative['creative_id']
                if c_id in creative_ids:
                    errors['adverts'] = 'Facebook strategy couldn\'t have duplicate creatives.'
                    return errors
                else:
                    creative_ids.append(c_id)

        return errors

    def is_valid(self, bundle, request=None):
        errors = StrategyForm(bundle.data).errors

        search_errors = self.check_duplicates(bundle, self.searchFields, True)
        advert_errors = self.check_advert_custom_trackers(bundle)
        landing_errors = self.check_landing_sites_amount(bundle)
        creative_errors = self.check_fb_creative_duplicates(bundle)
        creative_errors.update(self.check_advert_creative_destination(bundle))
        errors.update(search_errors)
        errors.update(advert_errors)
        errors.update(landing_errors)
        errors.update(creative_errors)

        return errors
