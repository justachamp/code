
from ui.common.states import BaseState


class CREATIVE_STATE:
    # kanary statuses
    audited = 'audited'
    rejected = 'rejected'
    blocked = 'blocked'  # Audit blocked because of lack of funds
    pending = 'pending'
    expired = 'expired'
    pending_pre_audit = 'pending pre-audit'
    rejected_pre_audit = 'rejected pre-audit'


class BRAND_STATE:
    pending = 'pending'
    confirmed = 'confirmed'
    rejected = 'rejected'
    not_exists = confirmed

# mapping from appnexus statuses to kanary statuses
STATUS_STATE_MAP = {
    'n': CREATIVE_STATE.pending,
    'p': CREATIVE_STATE.pending,
    'r': CREATIVE_STATE.rejected,
    'u': CREATIVE_STATE.rejected,
    'e': CREATIVE_STATE.expired,
    'a': CREATIVE_STATE.audited,
    'fa': CREATIVE_STATE.audited,
    'fp': CREATIVE_STATE.pending_pre_audit,
    'fr': CREATIVE_STATE.rejected_pre_audit,
}


class LiverailStatus:
    pending = 'pending'
    uploaded = 'uploaded'
    # Status when error ocurred
    error = 'error'

    # Active means: after creative is successfully encoded.
    active = 'active'


LIVERAIL_STATUS_CHOICES = ((LiverailStatus.pending, LiverailStatus.pending),
                           (LiverailStatus.uploaded, LiverailStatus.uploaded),
                           (LiverailStatus.error, LiverailStatus.error),
                           (LiverailStatus.active, LiverailStatus.active))


class CreativeState(BaseState):

    def __init__(self, creative, *args, **kwargs):
        self.creative = creative

    @property
    def status(self):
        if self.blocked:
            return CREATIVE_STATE.blocked
        else:
            return STATUS_STATE_MAP[self.appnexus_status]

    @property
    def appnexus_status(self):
        '''AppNexus audit status'''
        return self.creative.appnexus_status

    @property
    def brand_status(self):
        """ AppNexus brand page access status for Facebook newsfeed creatives. """
        if self.creative.is_facebook_destination(verify_is_newsfeed=True):
            return self.creative.brand.appnexus_access_status
        else:
            return BRAND_STATE.not_exists

    # "own" properties (related only to creative)
    @property
    def audited(self):
        return STATUS_STATE_MAP[self.appnexus_status] == CREATIVE_STATE.audited

    @property
    def rejected(self):
        return STATUS_STATE_MAP[self.appnexus_status] == CREATIVE_STATE.rejected

    @property
    def pending(self):
        return STATUS_STATE_MAP[self.appnexus_status] == CREATIVE_STATE.pending

    @property
    def blocked(self):
        return self.pending and self.creative.appnexus_audit_blocked_no_funds

    @property
    def expired(self):
        return STATUS_STATE_MAP[self.appnexus_status] == CREATIVE_STATE.expired

    @property
    def brand_page_confirmed(self):
        return self.brand_status == BRAND_STATE.confirmed

    @property
    def brand_page_rejected(self):
        return self.brand_status == BRAND_STATE.rejected

    def to_dict(self):
        bools = ['audited', 'rejected', 'pending', 'blocked', 'expired']
        lists = []

        return self._make_state_dict(self, bools, lists)
