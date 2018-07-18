from enum import Enum
from copy import deepcopy

styles = [
    'icon-medium-horizontal',
    'icon-small-horizontal',
    'icon-big-vertical',
    'icon-big-horizontal-shares',
    'label-horizontal',
    'icon-medium-horizontal-shares',
    'icon-big-vertical-shares',
    'label-horizontal-transparent',
    'icon-medium-horizontal-side-shares',
    'label-horizontal-shares',
    # Unused styles
    #     'icon-medium-vertical',
    #     'icon-small-horizontal-shares',
]


WIDGET_CONFIGURATION_SHARING_BUTTONS = 'sharing-buttons'
WIDGET_CONFIGURATION_ORIGIN_BUTTONS = 'origin-buttons'
WIDGET_CONFIGURATION_COPY_PASTE = 'copy-paste'
WIDGET_CONFIGURATION_NEWSLETTER = 'newsletter'
WIDGET_CONFIGURATION_MOBILE = 'mobile'
WIDGET_CONFIGURATION_FOLLOW = 'follow-buttons'
WIDGET_CONFIGURATION_VERTICAL_FLOAT = 'vertical-float'
WIDGET_CONFIGURATION_CIRCULAR_MOBILE = 'circular-mobile'

WIDGET_CONFIGURATION_TYPE_CHOICES = (
    (WIDGET_CONFIGURATION_SHARING_BUTTONS, 'Sharing buttons'),
    (WIDGET_CONFIGURATION_ORIGIN_BUTTONS, 'Origin buttons'),
    (WIDGET_CONFIGURATION_COPY_PASTE, 'Copy-paste'),
    (WIDGET_CONFIGURATION_NEWSLETTER, 'Newsletter'),
    (WIDGET_CONFIGURATION_MOBILE, 'Mobile'),
    (WIDGET_CONFIGURATION_FOLLOW, 'Follow buttons'),
    (WIDGET_CONFIGURATION_VERTICAL_FLOAT, 'Vertical float'),
    (WIDGET_CONFIGURATION_CIRCULAR_MOBILE, 'Circular Mobile')
)


BUTTON_ORIENTATION_VERTICAL = 'vertical'
BUTTON_ORIENTATION_HORIZONTAL = 'horizontal'

BUTTON_ORIENTATION_CHOICES = (
    (BUTTON_ORIENTATION_VERTICAL, 'Vertical'),
    (BUTTON_ORIENTATION_HORIZONTAL, 'Horizontal'),
)

WIDGET_LEFT_POSITION = 'left'
WIDGET_RIGHT_POSITION = 'right'
WIDGET_TOP_POSITION = 'top'
WIDGET_BOTTOM_POSITION = 'bottom'
WIDGET_TOP_LEFT_POSITION = 'top-left'
WIDGET_BOTTOM_LEFT_POSITION = 'bottom-left'
WIDGET_TOP_RIGHT_POSITION = 'top-right'
WIDGET_BOTTOM_RIGHT_POSITION = 'bottom-right'

WIDGET_POSITIONS = (
    (WIDGET_LEFT_POSITION, 'Left'),
    (WIDGET_RIGHT_POSITION, 'Right'),
    (WIDGET_TOP_POSITION, 'Top'),
    (WIDGET_BOTTOM_POSITION, 'Bottom'),
    (WIDGET_TOP_LEFT_POSITION, 'Top Left'),
    (WIDGET_BOTTOM_LEFT_POSITION, 'Bottom Left'),
    (WIDGET_TOP_RIGHT_POSITION, 'Top Right'),
    (WIDGET_BOTTOM_RIGHT_POSITION, 'Bottom Right'),
)


BUTTON_SIZE_SMALL = 'small'
BUTTON_SIZE_MEDIUM = 'medium'
BUTTON_SIZE_BIG = 'big'
BUTTON_SIZE_LARGE = 'large'

BUTTON_SIZE_CHOICES = (
    (BUTTON_SIZE_SMALL, 'Small'),
    (BUTTON_SIZE_MEDIUM, 'Medium'),
    (BUTTON_SIZE_BIG, 'Big'),
    (BUTTON_SIZE_LARGE, 'Large'),
)


BUTTON_STYLE_ICON = 'icon'
BUTTON_STYLE_LABEL = 'label'
BUTTON_STYLE_COUNTER = 'counter'

BUTTON_STYLE_CHOICES = (
    (BUTTON_STYLE_ICON, 'Icon'),
    (BUTTON_STYLE_LABEL, 'Label'),
    (BUTTON_STYLE_COUNTER, 'Counter'),
)


COUNTER_POSITION_TOP = 'top'
COUNTER_POSITION_RIGHT = 'right'

COUNTER_POSITION_CHOICES = (
    (COUNTER_POSITION_TOP, 'Top'),
    (COUNTER_POSITION_RIGHT, 'Right')
)


SOCIAL_SERVICE_FACEBOOK = 'facebook'
SOCIAL_SERVICE_TWITTER = 'twitter'
SOCIAL_SERVICE_GOOGLE_PLUS = 'googlePlus'
SOCIAL_SERVICE_LINKEDIN = 'linkedin'
SOCIAL_SERVICE_PINTEREST = 'pinterest'
SOCIAL_SERVICE_INSTAGRAM = 'instagram'
SOCIAL_SERVICE_DIGG = 'digg'
SOCIAL_SERVICE_DELICIOUS = 'delicious'
SOCIAL_SERVICE_STUMBLEUPON = 'stumbleupon'
SOCIAL_SERVICE_GMAIL = 'gmail'
SOCIAL_SERVICE_WHATSAPP = 'whatsapp'
SOCIAL_SERVICE_REDDIT = 'reddit'
SOCIAL_SERVICE_TUMBLR = 'tumblr'
SOCIAL_SERVICE_SMS = 'sms'
SOCIAL_SERVICE_FACEBOOK_MESSENGER = 'facebook-messenger'
SOCIAL_SERVICE_FACEBOOK_LIKE = 'facebook-like'
SOCIAL_SERVICE_YOUTUBE = 'youtube'
SOCIAL_SERVICE_WEIBO = 'weibo'
SOCIAL_SERVICE_LINE = 'line'

FACEBOOK_FOLLOW = 'facebook_follow'
INSTAGRAM_FOLLOW = 'instagram_follow'
TWITTER_FOLLOW = 'twitter_follow'
PINTEREST_FOLLOW = 'pinterest_follow'
YOUTUBE_SUBSCRIBE = 'youtube_subscribe'
GOOGLE_PLUS_ONE = 'googlePlus_one'
LINKEDIN_FOLLOW = 'linkedin_follow'

SOCIAL_SERVICE_CHOICES = (
    (SOCIAL_SERVICE_FACEBOOK, 'Facebook'),
    (SOCIAL_SERVICE_TWITTER, 'Twitter'),
    (SOCIAL_SERVICE_GOOGLE_PLUS, 'Google+'),
    (SOCIAL_SERVICE_LINKEDIN, 'LinkedIn'),
    (SOCIAL_SERVICE_PINTEREST, 'Pinterest'),
    (SOCIAL_SERVICE_INSTAGRAM, 'Instagram'),
    (SOCIAL_SERVICE_DIGG, 'Digg'),
    (SOCIAL_SERVICE_DELICIOUS, 'Delicious'),
    (SOCIAL_SERVICE_STUMBLEUPON, 'StumbleUpon'),
    (SOCIAL_SERVICE_GMAIL, 'Gmail'),
    (SOCIAL_SERVICE_WHATSAPP, 'WhatsApp'),
    (SOCIAL_SERVICE_REDDIT, 'Reddit'),
    (SOCIAL_SERVICE_TUMBLR, 'Tumblr'),
    (SOCIAL_SERVICE_SMS, 'SMS'),
    (SOCIAL_SERVICE_FACEBOOK_MESSENGER, 'Facebook Messenger'),
    (SOCIAL_SERVICE_FACEBOOK_LIKE, 'Facebook Like'),
    (SOCIAL_SERVICE_YOUTUBE, 'Youtube'),
    (SOCIAL_SERVICE_WEIBO, 'Weibo'),
    (SOCIAL_SERVICE_LINE, 'Line'),
)

SOURCE_EMAIL = 'email'
SOURCE_DARK_SOCIAL = 'darkSocial'
SOURCE_COPY_LINK = 'copyLink'

BUTTONS_SOURCE_SET = deepcopy(SOCIAL_SERVICE_CHOICES)
BUTTONS_SOURCE_SET = list(BUTTONS_SOURCE_SET)
BUTTONS_SOURCE_SET.extend([(SOURCE_EMAIL, 'Email')])
BUTTONS_SOURCE_SET = tuple(BUTTONS_SOURCE_SET)

SOURCE_SET = set(dict(BUTTONS_SOURCE_SET).keys() + [SOURCE_DARK_SOCIAL, SOURCE_COPY_LINK])


class Events(Enum):
    SHARE = 'share'
    CLICK = 'click'
    VIEW = 'view'
    FOLLOW = 'follow'
    COPY = 'copy'


class Tools(Enum):
    ADDRESS_BAR = 'address-bar'
    COPY_PASTE = 'copy-paste'
    SHARING_BUTTONS = 'sharing-buttons'
    NEWSLETTER_SHARING_BUTTONS = 'newsletter-sharing-buttons'
    FOLLOW_BUTTONS = 'follow-buttons'


UNKNOWN_COUNTRY = 'unknown'
UNKNOWN_BROWSER = 'Other'
