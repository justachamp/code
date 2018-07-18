from etc.constants import FRONTEND_LIVE_VIEW_PERIOD_SECONDS
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from ui.utils import render_to_json
from ui.liveview.models import LiveViewCounter
from ui.campaign.models import Campaign, Strategy, Advert


class LiveViewDataSource(object):
    ''' Live reports data source for active campaigns, strategies and adverts. '''

    def __init__(self, model_name, account):
        '''
        Initialize data source
            :param str model_name: Model name, 'Campaign', 'Strategy' or 'Advert
            :param Account account: Owner of db entries
        '''
        self.model_name = model_name.lower()
        self.account = account

    @property
    def active_objects(self):
        '''
        Returns list of objects with running state

        :returns: list of Campaign, Strategy or Advert objects
        :rtype: list
        '''
        active_objects = None
        if self.model_name == 'campaign':
            active_objects = Campaign.objects_visible.filter(account=self.account)
        elif self.model_name == 'strategy':
            active_objects = Strategy.objects_visible.filter(campaign__account=self.account)
        elif self.model_name == 'advert':
            strategies = Strategy.objects_visible.filter(campaign__account=self.account).values('id')
            active_objects = Advert.objects.filter(strategy__id__in=strategies)
        else:
            return []
        return filter(lambda o: o.state.is_running, active_objects.all())

    def get_metrics(self):
        '''
        Get live view metrics for active objects

        :returns: list of dictionaries like:
            {'public_id': '0', 'name': 'Campaign One', imp: '4', bid: '10', winbid_ratio" '40.0%'}
        :rtype: list
        '''
        active_objects = self.active_objects
        active_object_ids = [o.public_id for o in self.active_objects]

        time_from = datetime.utcnow() - timedelta(seconds=FRONTEND_LIVE_VIEW_PERIOD_SECONDS)

        # Add time filtering
        metrics = LiveViewCounter.objects.filter(public_id__in=active_object_ids)\
            .filter(time__gt=time_from)\
            .values('public_id')\
            .annotate(imp=Sum('imp'), bid=Sum('bid'))

        metrics_mapping = {m['public_id']: m for m in metrics}

        def join_object_with_metric(related_object):
            public_id = related_object.public_id
            metric = {'public_id': public_id, 'imp': 0, 'bid': 0}
            metric.update(metrics_mapping.get(public_id, {}))
            winbid_ratio = float(metric['imp']) / metric['bid'] if metric['bid'] else 0
            metric.update({
                'name': related_object.full_name,
                'winbid_ratio': '{0:.1%}'.format(winbid_ratio)
            })
            return metric

        return map(join_object_with_metric, active_objects)


@render_to_json(preserve_http_response=True)
@login_required
def liveview(request, model_name):
    data_source = LiveViewDataSource(model_name, request.user.account)

    return [metric for metric in data_source.get_metrics()]
