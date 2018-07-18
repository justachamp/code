(function() {
  'use strict';

  function Enums() {
    this.BUTTON_SIZES = ['small', 'medium', 'large', 'big'];
    this.SERVICE_BUTTONS = [
      {service: 'facebook', text: 'Facebook'},
      {service: 'twitter', text: 'Twitter'},
      {service: 'linkedin', text: 'LinkedIn'},
      {service: 'pinterest', text: 'Pinterest'},
      {service: 'googlePlus', text: 'Google+'},
      {service: 'whatsapp', text: 'WhatsApp'},
      {service: 'sms', text: 'SMS'},
      {service: 'digg', text: 'Digg'},
      {service: 'delicious', text: 'Delicious'},
      {service: 'stumbleupon', text: 'Stumbleupon'},
      {service: 'gmail', text: 'GMail'},
      {service: 'tumblr', text: 'Tumblr'},
      {service: 'email', text: 'Email'},
      {service: 'reddit', text: 'Reddit'},
      {service: 'weibo', text: 'Weibo'},
      {service: 'line', text: 'Line'}
    ];

    this.NEWSLETTER_SERVICE_BUTTONS = [
      {service: 'facebook', text: 'Facebook'},
      {service: 'twitter', text: 'Twitter'},
      {service: 'linkedin', text: 'LinkedIn'},
      {service: 'pinterest', text: 'Pinterest'},
      {service: 'googlePlus', text: 'Google+'},
      {service: 'digg', text: 'Digg'},
      {service: 'delicious', text: 'Delicious'},
      {service: 'stumbleupon', text: 'Stumbleupon'},
      {service: 'gmail', text: 'GMail'},
      {service: 'reddit', text: 'Reddit'},
      {service: 'tumblr', text: 'Tumblr'},
      {service: 'weibo', text: 'Weibo'}
    ];

    //cannot get event from default share button
    this.ORIGIN_SERVICE_BUTTONS = [

      //{service: 'facebook', text: 'Facebook Share'},
      {service: 'facebook-messenger', text: 'Facebook Send'},
      {service: 'facebook-like', text: 'Facebook Like'},
      {service: 'googlePlus', text: 'Google+'},
      {service: 'twitter', text: 'Twitter'}
    ];
    this.FOLLOW_BUTTONS = [
      {service: 'facebook', text: 'Facebook', placeholder: 'http://facebook.com/..'},
      {service: 'twitter', text: 'Twitter', placeholder: 'http://twitter.com/..'},
      {service: 'linkedin', text: 'LinkedIn', placeholder: 'http://linkedin.com/..'},
      {service: 'pinterest', text: 'Pinterest', placeholder: 'http://pinterest.com/..'},
      {service: 'instagram', text: 'Instagram', placeholder: 'http://instagram.com/..'},
      {service: 'googlePlus', text: 'Google+', placeholder: 'http://plus.google.com/..'},
      {service: 'youtube', text: 'Youtube', placeholder: 'http://youtube.com/..'}
    ];
    this.VERTICAL_FLOAT_BUTTONS = [
      {service: 'facebook', text: 'Facebook', placeholder: 'http://facebook.com/..'},
      {service: 'twitter', text: 'Twitter', placeholder: 'http://twitter.com/..'},
      {service: 'linkedin', text: 'LinkedIn', placeholder: 'http://linkedin.com/..'},
      {service: 'pinterest', text: 'Pinterest', placeholder: 'http://pinterest.com/..'},
      {service: 'googlePlus', text: 'Google+', placeholder: 'http://plus.google.com/..'}
    ];
    this.SHARING_BUTTONS = {
      label: 'Sharing Buttons',
      value: 'sharing-buttons',
      maxWidgets: 0,
      image: 'assets/images/post.png'
    };
    this.ORIGIN_BUTTONS = {
      label: 'Original Buttons',
      value: 'origin-buttons',
      maxWidgets: 0,
      image: 'assets/images/post.png'
    };
    this.COPY_PASTE = {
      label: 'Copy-Paste',
      value: 'copy-paste',
      maxWidgets: 1,
      image: 'assets/images/copypaste.png'
    };
    this.NEWSLETTER = {
      label: 'Newsletter',
      value: 'newsletter',
      maxWidgets: 1,
      image: 'assets/images/newsletter.png'
    };
    this.MOBILE = {
      label: 'Mobile',
      value: 'mobile',
      maxWidgets: 1,
      image: 'assets/images/mobile.png'
    };
    this.FOLLOW_BUTTON = {
      label: 'Follow',
      value: 'follow-buttons',
      maxWidgets: 0,
      image: 'assets/images/follow.png'
    };
    this.VERTICAL_FLOAT = {
      label: 'Vertical Float',
      value: 'vertical-float',
      maxWidgets: 1,
      image: 'assets/images/sidebar.png'
    };
    this.CIRCULAR_MOBILE = {
      label: 'Circular Mobile',
      value: 'circular-mobile',
      maxWidgets: 1,
      image: 'assets/images/circular-mobile.png'
    };
    this.WIDGET_TYPES = [
      this.SHARING_BUTTONS,
      this.ORIGIN_BUTTONS,
      this.COPY_PASTE,
      this.NEWSLETTER,
      this.MOBILE,
      this.CIRCULAR_MOBILE,
      this.FOLLOW_BUTTON,
      this.VERTICAL_FLOAT
    ];
  }

  angular.module('angulardash.common')
    .service('Enums', Enums);
})();
