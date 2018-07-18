import simplejson
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from ui.campaign.models import Strategy


@login_required
def strategy_toggle_active(request, id):
    ''' Toggles is_paused parameter of a given strategy. '''
    strategy = get_object_or_404(Strategy, id=id, campaign__account__users=request.user)

    if not request.user.account.id == strategy.campaign.account.id:
        return HttpResponse(status=403)

    strategy.is_paused = not strategy.is_paused
    strategy.save()

    return HttpResponse(
        simplejson.dumps({'is_paused': strategy.is_paused}),
        mimetype='application/json'
    )
