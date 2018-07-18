'use strict';

function configuration($httpProvider) {
  $httpProvider.interceptors.push(['$rootScope', '$q', function($rootScope, $q) {
    return {
      response: function(r) {
        console.log(r.status.toString(), r.config.method, r.config.url, r.config.params);
        return r || $q.when(r);
      },

      responseError: function(r) {
        if (r.status) {
          console.log(r.status.toString(), r.config.method, r.config.url, r.config.params);
        }

        return $q.reject(r);
      },

      request: function(r) {
        if (r.data) {
          console.log('BODY', r.method, r.url, r.data, r.headers);
        }

        return r || $q.when(r);
      }
    };
  }]);
}

function runHandler(loginBackend, $httpBackend, AppSettings) {
  // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
  loginBackend.config(
    function(method, url, data) {
      return data.email;
    },

    function(status, data) {
      if (status === 200 && typeof data.token === 'string') {
        return data.token;
      } else {
        throw Error('Unexpected response');
      }
    },

    function(status, data, headers, statusText, session) {
      if (session !== undefined && data.hasOwnProperty('token')) {
        data.token = session;
      }

      return [status, data, headers, statusText];
    },

    function(session) {
      var result = {
        Accept: 'application/json, text/plain, */*'
      };

      if (session) {
        result.Authorization = 'JWT ' + session;
      }

      return result;
    }

  );

  var pages = [
      {label: 'clearcode.cc'},
      {label: 'piwik.pro'},
      {label: 'gravity4.com'}
    ];
  var backendApi = AppSettings.backendApi;
  var widgetPrefix = '/';

  function getDigestQuery(siteId) {
    return new RegExp(backendApi + 'reports\\?(begin_date=([0-9])+&)&(end_date=([0-9])+&)&site=' + siteId);
  }

  //Login User
  loginBackend.when(
    'POST',
    backendApi + 'tokens',
    {
      email: 'test@test.pl',
      password: '123qwe'
    }
  ).respond(
    200,
    {
      token: '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
    }
  );

  $httpBackend.whenPOST(
    backendApi + 'tokens',
    {
      email: 'nonExistingUser@test.pl',
      password: 'none'
    }
  ).respond(
    400,
    {
      non_field_errors: ['Unable to login with provided credentials.']
    }
  );

  //Register User
  $httpBackend.whenPOST(
    backendApi + 'users',
    {
      email: 'newUser@test.pl',
      password: 'new password'
    }
  ).respond(
    201,
    {
      id: 5,
      email: 'newUser@test.pl'
    }
  );

  $httpBackend.whenPOST(
    backendApi + 'users',
    {
      email: 'test@test.pl',
      password: '123qwe'
    }
  ).respond(
    400,
    {
      email: ['This field must be unique.']
    }
  );

  //new user should verify email
  $httpBackend.whenPOST(
    backendApi + 'tokens',
    {
      email: 'not_verified@test.pl',
      password: '123qwe'
    }
  ).respond(
    400,
    {
      non_field_errors: ['You need to verify your account before logging in.']
    }
  );

  //Reset Password (first step)
  $httpBackend.whenPOST(
    backendApi + 'users/reset_password',
    {
      email: 'verified@test.pl'
    }
  ).respond(204, '');

  $httpBackend.whenPOST(
    backendApi + 'users/reset_password',
    {
      email: 'bot@bot.pl'
    },
    undefined,
    {
      extraHeaders: {
        'x-bot': '1'
      }
    }
  ).respond(
    429,
    {
      detail: 'Request was throttled. Expected available in 1.0 second.'
    },
    {
      'Retry-After': 1
    }
  );

  $httpBackend.whenPOST(
    backendApi + 'users/reset_password',
    {
      email: 'not_verified@test.pl'
    }
  ).respond(
    400,
    {
      email: ['Email is not verified']
    }
  );

  $httpBackend.whenPOST(
    backendApi + 'users/reset_password',
    {
      email: 'nonExistingUser@test.pl'
    }
  ).respond(
    400,
    {
      email: ['Email not found']
    }
  );

  //Reset Password (second step) //TODO on backend side
  $httpBackend.whenPOST(
    backendApi + 'users/change_password',
    {
      token: '3|valid',
      password: 'newPassword'
    }
  ).respond(204, '');

  $httpBackend.whenPOST(
    backendApi + 'users/change_password',
    {
      token: 'botToken',
      password: 'newPassword'
    },
    undefined,
    {
      extraHeaders: {
        'x-bot': '1'
      }
    }
  ).respond(
    429,
    {
      detail: 'Request was throttled. Expected available in 1.0 second.'
    },
    {
      'Retry-After': 1
    }
  );

  $httpBackend.whenPOST(
    backendApi + 'users/change_password',
    {
      token: 'invalid',
      password: 'whatever'
    }
  ).respond(
    400,
    {
      token: ['Token is invalid']
    }
  );

  // Get all pages for user
  $httpBackend.whenGET(
    backendApi + 'pages/',
    undefined,
    {
      skip: true
    }
  ).respond(pages);

  // Get all sites
  $httpBackend.whenGET(
    backendApi + 'sites',
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {
        address_bar_sharing: false,
        copy_paste_sharing: false,
        trim_api_key: '1254856352048jwdf285',
        has_short_urls: true,
        domain: 'test.pl.domain.com',
        id: 1,
        hash_id: '1:04Q7fqXxgLx5HMtyPnXI8AWqDNY',
        thank_you_message: '',
        social_urls: [],
        analytics_account: '',
        analytics_profile: '',
        analytics_property: ''
      },
      {
        address_bar_sharing: true,
        copy_paste_sharing: true,
        has_short_urls: true,
        trim_api_key: '1shh463520sgjw2f28w',
        domain: 'test.pl.domain.with.social.urls.com',
        id: 2,
        hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
        thank_you_message: 'thank you msg',
        social_urls: [{
          id: 1,
          service: 'facebook',
          url: 'http://facebook.com/url'
        }],
        analytics_account: '',
        analytics_profile: '',
        analytics_property: ''
      }
    ]
  );

  // Get site 1
  $httpBackend.whenGET(
    backendApi + 'sites/1',
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      address_bar_sharing: false,
      copy_paste_sharing: false,
      has_short_urls: true,
      trim_api_key: '1254856352048jwdf285',
      domain: 'test.pl.domain.com',
      id: 1,
      hash_id: '1:04Q7fqXxgLx5HMtyPnXI8AWqDNY',
      thank_you_message: '',
      social_urls: [],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    }
  );

  // Get site 2
  $httpBackend.whenGET(
    backendApi + 'sites/2',
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      address_bar_sharing: true,
      copy_paste_sharing: true,
      has_short_urls: true,
      trim_api_key: '1shh463520sgjw2f28w',
      domain: 'test.pl.domain.with.social.urls.com',
      id: 2,
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      thank_you_message: 'thank you msg',
      social_urls: [{
        id: 1,
        service: 'facebook',
        url: 'http://facebook.com/url'
      }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    }
  );

  // Create site without credentials
  $httpBackend.whenPOST(
    backendApi + 'sites',
    {
      domain: 'some.domain.com'
    },
    {}
  ).respond(
    401,
    {
      detail: 'Authentication credentials were not provided.'
    }
  );

  // Create site without social urls
  $httpBackend.whenPOST(
    backendApi + 'sites',
    {
      domain: 'some.domain.com'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    201,
    {
      address_bar_sharing: false,
      copy_paste_sharing: false,
      has_short_urls: true,
      trim_api_key: '',
      domain: 'some.domain.com',
      id: 3,
      hash_id: '3:E623eJaunzzoR39K1sXC9B0HVH8',
      thank_you_message: '',
      social_urls: [],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    },
    undefined,
    undefined,
    function(status, data, headers, statusText) {
      if (typeof data.id === 'number') {
        data.id = 3;
      }

      return [status, data, headers, statusText];
    }

  );

  // Create site: nested errors for social urls
  $httpBackend.whenPOST(
    backendApi + 'sites',
    {
      domain: '',
      social_urls:  [
        {   // valid
          url: 'http://www.valid.com',
          service: 'facebook'
        },
        {}, // empty
        {   // invalid
          url: 'http://www.valid.com',
          service: 'non_valid'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      domain: [
        'This field may not be blank.'
      ],
      social_urls: [
        {},
        {
          url: [
            'This field is required.'
          ],
          service: [
            'This field is required.'
          ]
        },
        {
          service: [
            '"non_valid" is not a valid choice.'
          ]
        }
      ]
    }
  );

  // Create site with duplicate social url service
  $httpBackend.whenPOST(
    backendApi + 'sites',
    {
      domain: 'another.domain.com',
      social_urls:  [
        {
          url: 'http://www.service.com',
          service: 'facebook'
        },
        {
          url: 'http://www.duplicate.service.com',
          service: 'facebook'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      social_urls: [
        'Service must be unique for the site.'
      ]
    }
  );

  // Create site with social urls
  $httpBackend.whenPOST(
    backendApi + 'sites',
    {
      domain: 'another.domain.com',
      social_urls: [{
        service: 'facebook',
        url: 'http://facebook.com/url'
      }]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    201,
    {
      address_bar_sharing: false,
      copy_paste_sharing: false,
      has_short_urls: true,
      trim_api_key: '',
      domain: 'another.domain.com',
      id: 3,
      hash_id: '3:E623eJaunzzoR39K1sXC9B0HVH8',
      thank_you_message: '',
      social_urls: [{
        id: 2,
        service: 'facebook',
        url: 'http://facebook.com/url'
      }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    },
    undefined,
    undefined,
    function(status, data, headers, statusText) {
      if (typeof data.id === 'number') {
        data.id = 3;
      }

      if (data.social_urls && typeof data.social_urls[0].id === 'number') {
        data.social_urls[0].id = 2;
      }

      return [status, data, headers, statusText];
    }

  );

  // Create site with all social urls
  $httpBackend.whenPOST(
    backendApi + 'sites',
    {
      domain: 'another.domain.com',
      social_urls: [{
        service: 'facebook',
        url: 'http://facebook.com/url'
      },
        {
          service: 'googlePlus',
          url: 'http://google.com/url'
        },
        {
          service: 'linkedin',
          url: 'http://linkedin.com/url'
        },
        {
          service: 'pinterest',
          url: 'http://pinterest.com/url'
        },
        {
          service: 'twitter',
          url: 'http://twitter.com/url'
        }]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    201,
    {
      address_bar_sharing: false,
      copy_paste_sharing: false,
      has_short_urls: true,
      trim_api_key: '',
      domain: 'another.domain.com',
      id: 3,
      hash_id: '3:E623eJaunzzoR39K1sXC9B0HVH8',
      thank_you_message: '',
      social_urls: [{
        id: 2,
        service: 'facebook',
        url: 'http://facebook.com/url'
      },
        {
          id: 3,
          service: 'googlePlus',
          url: 'http://google.com/url'
        },
        {
          id: 4,
          service: 'linkedin',
          url: 'http://linkedin.com/url'
        },
        {
          id: 5,
          service: 'pinterest',
          url: 'http://pinterest.com/url'
        },
        {
          id: 6,
          service: 'twitter',
          url: 'http://twitter.com/url'
        }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    },
    undefined,
    undefined,
    function(status, data, headers, statusText) {
      if (typeof data.id === 'number') {
        data.id = 3;
      }

      if (data.social_urls && typeof data.social_urls[0].id === 'number') {
        var count = 2;
        data.social_urls.forEach(function(url) {
          if (typeof url.id === 'number') {
            url.id = count++;
          }
        });
      }

      return [status, data, headers, statusText];
    }

  );

  // Update site address_bar_sharing
  $httpBackend.whenPATCH(
    backendApi + 'sites/2',
    {
      address_bar_sharing: false
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      address_bar_sharing: false,
      copy_paste_sharing: true,
      has_short_urls: true,
      trim_api_key: '1shh463520sgjw2f28w',
      domain: 'test.pl.domain.with.social.urls.com',
      id: 2,
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      thank_you_message: 'thank you msg',
      social_urls: [{
        id: 1,
        service: 'facebook',
        url: 'http://facebook.com/url'
      }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    }
  );

  // Update site api_key
  $httpBackend.whenPATCH(
    backendApi + 'sites/2',
    {
      trim_api_key: '11111111111111111'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      address_bar_sharing: true,
      copy_paste_sharing: true,
      has_short_urls: true,
      trim_api_key: '11111111111111111',
      domain: 'test.pl.domain.with.social.urls.com',
      id: 2,
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      thank_you_message: 'thank you msg',
      social_urls: [{
        id: 1,
        service: 'facebook',
        url: 'http://facebook.com/url'
      }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    }
  );

  // Update site domain
  $httpBackend.whenPATCH(
    backendApi + 'sites/2',
    {
      domain: 'new.domain.com'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      address_bar_sharing: true,
      copy_paste_sharing: true,
      has_short_urls: true,
      trim_api_key: '1shh463520sgjw2f28w',
      domain: 'new.domain.com',
      id: 2,
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      thank_you_message: 'thank you msg',
      social_urls: [{
        id: 1,
        service: 'facebook',
        url: 'http://facebook.com/url'
      }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    }
  );

  // Update site thank_you_message
  $httpBackend.whenPATCH(
    backendApi + 'sites/2',
    {
      thank_you_message: 'new thank you msg'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      address_bar_sharing: true,
      copy_paste_sharing: true,
      has_short_urls: true,
      trim_api_key: '1shh463520sgjw2f28w',
      domain: 'test.pl.domain.with.social.urls.com',
      id: 2,
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      thank_you_message: 'new thank you msg',
      social_urls: [{
        id: 1,
        service: 'facebook',
        url: 'http://facebook.com/url'
      }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    }
  );

  // Update site
  $httpBackend.whenPATCH(
    backendApi + 'sites/2',
    {},
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      address_bar_sharing: true,
      copy_paste_sharing: true,
      has_short_urls: true,
      trim_api_key: '1shh463520sgjw2f28w',
      domain: 'test.pl.domain.with.social.urls.com',
      id: 2,
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      thank_you_message: 'thank you msg',
      social_urls: [{
        id: 1,
        service: 'facebook',
        url: 'http://facebook.com/url'
      }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    }
  );

  // Update site social_urls
  $httpBackend.whenPATCH(
    backendApi + 'sites/2',
    {
      social_urls: [{
        service: 'googlePlus',
        url: 'http://google.com/url'
      },
        {
          service: 'linkedin',
          url: 'http://linkedin.com/url'
        }]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      address_bar_sharing: true,
      copy_paste_sharing: true,
      has_short_urls: true,
      trim_api_key: '1shh463520sgjw2f28w',
      domain: 'test.pl.domain.with.social.urls.com',
      id: 2,
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      thank_you_message: 'thank you msg',
      social_urls: [{
        id: 2,
        service: 'googlePlus',
        url: 'http://google.com/url'
      },
        {
          id: 3,
          service: 'linkedin',
          url: 'http://linkedin.com/url'
        }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    }
  );

  // Update site social_urls with invalid service
  $httpBackend.whenPATCH(
    backendApi + 'sites/2',
    {
      social_urls: [{
        service: 'google',
        url: 'http://google.com/url'
      }]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      social_urls: [{
        service: ['"google" is not a valid choice.']
      }]
    }
  );

  // Update site social_urls with duplicate service
  $httpBackend.whenPATCH(
    backendApi + 'sites/2',
    {
      social_urls:  [
        {
          url: 'http://www.service.com',
          service: 'facebook'
        },
        {
          url: 'http://www.duplicate.service.com',
          service: 'facebook'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      social_urls: [
        'Service must be unique for the site.'
      ]
    }
  );

  // Update site all fields
  $httpBackend.whenPATCH(
    backendApi + 'sites/2',
    {
      address_bar_sharing: false,
      trim_api_key: '1as234fdgg123ad',
      copy_paste_sharing: false,
      has_short_urls: true,
      domain: 'another.domain.com',
      thank_you_message: 'thank you message for another.domain.com',
      social_urls: [{
        service: 'facebook',
        url: 'http://facebook.com/anotherurl'
      },
        {
          service: 'googlePlus',
          url: 'http://google.com/anotherurl'
        },
        {
          service: 'linkedin',
          url: 'http://linkedin.com/anotherurl'
        },
        {
          service: 'pinterest',
          url: 'http://pinterest.com/anotherurl'
        },
        {
          service: 'twitter',
          url: 'http://twitter.com/anotherurl'
        }]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      address_bar_sharing: false,
      copy_paste_sharing: false,
      has_short_urls: true,
      trim_api_key: '1as234fdgg123ad',
      domain: 'another.domain.com',
      id: 2,
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      thank_you_message: 'thank you message for another.domain.com',
      social_urls: [{
        id: 1,
        service: 'facebook',
        url: 'http://facebook.com/anotherurl'
      },
        {
          id: 2,
          service: 'googlePlus',
          url: 'http://google.com/anotherurl'
        },
        {
          id: 3,
          service: 'linkedin',
          url: 'http://linkedin.com/anotherurl'
        },
        {
          id: 4,
          service: 'pinterest',
          url: 'http://pinterest.com/anotherurl'
        },
        {
          id: 5,
          service: 'twitter',
          url: 'http://twitter.com/anotherurl'
        }],
      analytics_account: '',
      analytics_profile: '',
      analytics_property: ''
    }
  );

  // Get all widget configurations
  $httpBackend.whenGET(
    backendApi + 'sites/1/widgets',
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {
        id: 1,
        name: 'default',
        orientation: 'horizontal',
        button_style: 'icon',
        button_size: 'medium',
        counter_position: 'right',
        type: 'sharing-buttons',
        is_active: true,
        buttons: [
          {
            service: 'facebook',
            isExtraButton: false,
            text: 'Facebook',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          },
          {
            service: 'twitter',
            isExtraButton: false,
            text: 'Twitter',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          }
        ],
        vanity_domain: ''
      },
      {
        id: 2,
        name: 'custom widget config',
        orientation: 'vertical',
        button_style: 'label',
        button_size: 'small',
        counter_position: 'top',
        type: 'sharing-buttons',
        is_active: true,
        buttons: [
          {
            service: 'googlePlus',
            isExtraButton: false,
            text: 'Google+',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          },
          {
            service: 'linkedin',
            isExtraButton: false,
            text: 'LinkedIn',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          },
          {
            service: 'facebook',
            isExtraButton: false,
            text: 'Facebook',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          }
        ],
        vanity_domain: ''
      },
      {
        id: 3,
        name: 'newsletter widget',
        orientation: 'horizontal',
        button_style: 'label',
        button_size: 'small',
        counter_position: 'top',
        page_url: 'test page url',
        page_title: 'test',
        type: 'newsletter',
        is_active: true,
        buttons: [
          {
            service: 'facebook',
            isExtraButton: false,
            text: 'Facebook',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          },
          {
            service: 'twitter',
            isExtraButton: false,
            text: 'Twitter',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          }
        ],
        vanity_domain: ''
      }
    ]
  );

  // Get widget configuration 1
  $httpBackend.whenGET(
    backendApi + 'sites/1/widgets/1',
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      id: 1,
      name: 'default',
      orientation: 'horizontal',
      button_style: 'icon',
      button_size: 'medium',
      counter_position: 'right',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'facebook',
          isExtraButton: false,
          text: 'Facebook',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'twitter',
          isExtraButton: false,
          text: 'Twitter',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        }
      ],
      vanity_domain: ''
    }
  );

  // Get widget configuration 2
  $httpBackend.whenGET(
    backendApi + 'sites/1/widgets/2',
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      id: 2,
      name: 'custom widget config',
      orientation: 'vertical',
      button_style: 'label',
      button_size: 'small',
      counter_position: 'top',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'googlePlus',
          isExtraButton: false,
          text: 'Google+',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'linkedin',
          isExtraButton: false,
          text: 'LinkedIn',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'facebook',
          isExtraButton: false,
          text: 'Facebook',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        }
      ],
      vanity_domain: ''
    }
  );

  // Get widget configuration 3
  $httpBackend.whenGET(
    backendApi + 'sites/1/widgets/3',
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      id: 3,
      name: 'newsletter widget',
      media_url: 'test media url',
      page_url: 'test page url',
      page_title: 'test',
      type: 'newsletter',
      button_style: 'label',
      counter_position: 'top',
      orientation: 'horizontal',
      button_size: 'small',
      is_active: true,
      buttons: [
        {
          service: 'facebook',
          isExtraButton: false,
          text: 'Facebook',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'twitter',
          isExtraButton: false,
          text: 'Twitter',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        }
      ],
      vanity_domain: ''
    }
  );

  // Create widget configuration without credentials
  $httpBackend.whenPOST(
    backendApi + 'sites/1/widgets',
    {
      name: 'another widget config',
      orientation: 'horizontal',
      button_style: 'label',
      button_size: 'medium',
      counter_position: 'top',
      media_url: '',
      page_url: '',
      page_title: '',
      is_active: true,
      type: 'sharing-buttons',
      buttons: [
        {
          service: 'facebook'
        },
        {
          service: 'linkedin'
        }
      ]
    },
    {}
  ).respond(
    401,
    {
      detail: 'Authentication credentials were not provided.'
    }
  );

  // Create widget configuration without buttons
  $httpBackend.whenPOST(
    backendApi + 'sites/1/widgets',
    {
      name: 'another widget config',
      orientation: 'horizontal',
      button_style: 'label',
      button_size: 'medium',
      counter_position: 'top',
      buttons: [],
      media_url: '',
      page_url: '',
      page_title: '',
      type: 'sharing-buttons',
      is_active: true
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      buttons: [
        'Widget configuration has no buttons.'
      ]
    }
  );

  // Create widget configuration with existing name
  $httpBackend.whenPOST(
    backendApi + 'sites/1/widgets',
    {
      name: 'default',
      orientation: 'horizontal',
      button_style: 'label',
      button_size: 'medium',
      counter_position: 'top',
      media_url: '',
      page_url: '',
      page_title: '',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'facebook'
        },
        {
          service: 'linkedin'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      non_field_errors: ['The fields user, name must make a unique set.']
    }
  );

  // Create widget configuration: nested errors for buttons
  $httpBackend.whenPOST(
    backendApi + 'sites/1/widgets',
    {
      name: '',
      orientation: 'non_valid',
      button_style: 'non_valid',
      button_size: 'non_valid',
      counter_position: 'non_valid',
      media_url: '',
      page_url: '',
      page_title: '',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {   // valid
          service: 'facebook'
        },
        {}, // empty
        {   // invalid
          service: 'non_valid'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      name: [
        'This field may not be blank.'
      ],
      orientation: [
        '"non_valid" is not a valid choice.'
      ],
      button_style: [
        '"non_valid" is not a valid choice.'
      ],
      button_size: [
        '"non_valid" is not a valid choice.'
      ],
      counter_position: [
        '"non_valid" is not a valid choice.'
      ],
      buttons: [
        {},
        {
          service: [
            'This field is required.'
          ]
        },
        {
          service: [
            '"non_valid" is not a valid choice.'
          ]
        }
      ]
    }
  );

  // Create widget configuration with duplicate button service
  $httpBackend.whenPOST(
    backendApi + 'sites/1/widgets',
    {
      name: 'another widget config',
      orientation: 'horizontal',
      button_style: 'label',
      button_size: 'medium',
      counter_position: 'top',
      media_url: '',
      page_url: '',
      page_title: '',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'facebook'
        },
        {
          service: 'facebook'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      buttons: [
        'Service must be unique for the widget configuration.'
      ]
    }
  );

  // Create widget configuration with buttons
  $httpBackend.whenPOST(
    backendApi + 'sites/1/widgets',
    {
      name: 'another widget config',
      orientation: 'horizontal',
      button_style: 'label',
      button_size: 'medium',
      counter_position: 'top',
      media_url: '',
      page_url: '',
      page_title: '',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'googlePlus'
        },
        {
          service: 'twitter'
        },
        {
          service: 'facebook'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    201,
    {
      id: 4,
      name: 'another widget config',
      orientation: 'horizontal',
      button_style: 'label',
      button_size: 'medium',
      counter_position: 'top',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'googlePlus',
          isExtraButton: false,
          text: 'Google+',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'twitter',
          isExtraButton: false,
          text: 'Twitter',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'facebook',
          isExtraButton: false,
          text: 'Facebook',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        }
      ],
      vanity_domain: ''
    },
    undefined,
    undefined,
    function(status, data, headers, statusText) {
      if (typeof data.id === 'number') {
        data.id = 4;
      }

      return [status, data, headers, statusText];
    }

  );

  // Update widget configuration name
  $httpBackend.whenPATCH(
    backendApi + 'sites/1/widgets/1',
    {
      name: 'new name'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      id: 1,
      name: 'new name',
      orientation: 'horizontal',
      button_style: 'icon',
      button_size: 'medium',
      counter_position: 'right',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'facebook',
          isExtraButton: false,
          text: 'Facebook',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'twitter',
          isExtraButton: false,
          text: 'Twitter',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        }
      ],
      vanity_domain: ''
    }
  );

  // Update widget configuration name on existing name
  $httpBackend.whenPATCH(
    backendApi + 'sites/1/widgets/1',
    {
      name: 'custom widget config'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      non_field_errors: ['The fields user, name must make a unique set.']
    }
  );

  // Update widget configuration choices
  $httpBackend.whenPATCH(
    backendApi + 'sites/1/widgets/1',
    {
      orientation: 'vertical',
      button_style: 'label',
      button_size: 'large',
      counter_position: 'top'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      id: 1,
      name: 'default',
      orientation: 'vertical',
      button_style: 'label',
      button_size: 'large',
      counter_position: 'top',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'facebook',
          isExtraButton: false,
          text: 'Facebook',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'twitter',
          isExtraButton: false,
          text: 'Twitter',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        }
      ],
      vanity_domain: ''
    }
  );

  // Update widget configuration buttons
  $httpBackend.whenPATCH(
    backendApi + 'sites/1/widgets/1',
    {
      buttons: [
        {
          service: 'twitter'
        },
        {
          service: 'facebook'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      id: 1,
      name: 'default',
      orientation: 'horizontal',
      button_style: 'icon',
      button_size: 'medium',
      counter_position: 'right',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'twitter',
          isExtraButton: false,
          text: 'Twitter',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'facebook',
          isExtraButton: false,
          text: 'Facebook',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        }
      ],
      vanity_domain: ''
    }
  );

  // Update widget configuration buttons on empty list of buttons
  $httpBackend.whenPATCH(
    backendApi + 'sites/1/widgets/1',
    {
      buttons: []
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      buttons: [
        'Widget configuration has no buttons.'
      ]
    }
  );

  // Update widget configuration buttons with invalid service
  $httpBackend.whenPATCH(
    backendApi + 'sites/1/widgets/1',
    {
      buttons: [{
        service: 'google'
      }]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      buttons: [{
        service: ['"google" is not a valid choice.']
      }]
    }
  );

  // Update widget configuration buttons with duplicate service
  $httpBackend.whenPATCH(
    backendApi + 'sites/1/widgets/1',
    {
      buttons: [
        {
          service: 'twitter'
        },
        {
          service: 'twitter'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      buttons: [
        'Service must be unique for the widget configuration.'
      ]
    }
  );

  // Update widget configuration all fields
  $httpBackend.whenPATCH(
    backendApi + 'sites/1/widgets/1',
    {
      name: 'new name',
      orientation: 'vertical',
      button_style: 'label',
      button_size: 'large',
      counter_position: 'top',
      media_url: '',
      page_url: '',
      page_title: '',
      type: 'sharing-buttons',
      buttons: [
        {
          service: 'twitter'
        },
        {
          service: 'facebook'
        }
      ]
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      id: 1,
      name: 'new name',
      orientation: 'vertical',
      button_style: 'label',
      button_size: 'large',
      counter_position: 'top',
      type: 'sharing-buttons',
      is_active: true,
      buttons: [
        {
          service: 'twitter',
          isExtraButton: false,
          text: 'Twitter',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        },
        {
          service: 'facebook',
          isExtraButton: false,
          text: 'Facebook',
          is_short_link: true,
          has_counter: true,
          follow_url: ''
        }
      ],
      vanity_domain: ''
    }
  );

  //Retrieving event_source_all data for site 1 report
  $httpBackend.whenGET(
    getDigestQuery(1),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {label: 'googlePlus', shares: 3000, clicks: 1234},
      {label: 'facebook', shares: 12300, clicks: 650},
      {label: 'twitter', shares: 1456, clicks: 123},
      {label: 'pinterest', shares: 102, clicks: 12},
      {label: 'linkedin', shares: 2345, clicks: 345},
      {label: 'other', shares: 45, clicks: 5}
    ]
  );

  //Retrieving event_source_all data for site 2 report
  $httpBackend.whenGET(
    getDigestQuery(2),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {label: 'googlePlus', shares: 789, clicks: 34},
      {label: 'facebook', shares: 1200, clicks: 206},
      {label: 'twitter', shares: 543, clicks: 93},
      {label: 'pinterest', shares: 123, clicks: 57},
      {label: 'linkedin', shares: 235, clicks: 38},
      {label: 'other', shares: 5, clicks: 0}
    ]
  );

  //Retrieving event_tool_all data for site 1 report
  $httpBackend.whenGET(
    getDigestQuery(1),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {label: 'copy-paste', shares: 2345, clicks: 123},
      {label: 'sharing-buttons', shares: 5432, clicks: 1234},
      {label: 'address-bar', shares: 878, clicks: 12}
    ]
  );

  //Retrieving event_tool_all data for site 2 report
  $httpBackend.whenGET(
    getDigestQuery(2),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {label: 'copy-paste', shares: 345, clicks: 765},
      {label: 'sharing-buttons', shares: 45, clicks: 871},
      {label: 'address-bar', shares: 5, clicks: 91}
    ]
  );

  //Retrieving event_month data for site 1 report
  $httpBackend.whenGET(
    getDigestQuery(1),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {shares: 134, clicks: 234, month: 1401},
      {shares: 178, clicks: 256, month: 1402},
      {shares: 190, clicks: 345, month: 1403},
      {shares: 185, clicks: 456, month: 1404},
      {shares: 155, clicks: 256, month: 1405},
      {shares: 256, clicks: 700, month: 1406},
      {shares: 356, clicks: 987, month: 1407},
      {shares: 98, clicks: 1056, month: 1408},
      {shares: 15, clicks: 965, month: 1409},
      {shares: 5, clicks: 865, month: 1410},
      {shares: 1, clicks: 545, month: 1411},
      {shares: 10, clicks: 325, month: 1412},
      {shares: 0, clicks: 487, month: 1501},
      {shares: 5, clicks: 65, month: 1502}
    ]
  );

  //Retrieving event_month data for site 2 report
  $httpBackend.whenGET(
    getDigestQuery(2),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {shares: 13, clicks: 34, month: 1401},
      {shares: 17, clicks: 56, month: 1402},
      {shares: 19, clicks: 45, month: 1403},
      {shares: 18, clicks: 56, month: 1404},
      {shares: 15, clicks: 56, month: 1405},
      {shares: 25, clicks: 30, month: 1406},
      {shares: 35, clicks: 87, month: 1407},
      {shares: 98, clicks: 56, month: 1408},
      {shares: 1, clicks: 65, month: 1409},
      {shares: 5, clicks: 65, month: 1410},
      {shares: 1, clicks: 45, month: 1411},
      {shares: 1, clicks: 25, month: 1412},
      {shares: 0, clicks: 87, month: 1501},
      {shares: 5, clicks: 5, month: 1502}
    ]
  );

  //Retrieving event_url_all data for site 1 report
  $httpBackend.whenGET(
    getDigestQuery(1),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [{
      clicks: 2343,
      shares: 1343,
      title: 'Contact',
      url: 'http://gravity4.com/contact/'
    },
      {
        clicks: 234,
        shares: 345,
        title: 'Team',
        url: 'http://gravity4.com/g4team/'
      },
      {
        clicks: 334,
        shares: 675,
        title: 'Labs',
        url: 'http://gravity4.com/labs/'
      },
      {
        clicks: 6334,
        shares: 4675,
        title: 'App Center',
        url: 'http://gravity4.com/app-center/'
      },
      {
        clicks: 12334,
        shares: 8675,
        title: 'Product',
        url: 'http://gravity4.com/product/'
      },
      {
        clicks: 334,
        shares: 675,
        title: 'Vision',
        url: 'http://gravity4.com/vision/'
      },
      {
        clicks: 7834,
        shares: 1275,
        title: 'Introducing #Belimitless',
        url: 'http://gravity4.com/blog/introducing-belimitless/'
      },
      {
        clicks: 3334,
        shares: 7512,
        title: 'Tom Brady Doesn\'t Rely on Luck. Why Do You?',
        url: 'http://gravity4.com/blog/tom-brady-super-bowl-sunday-doesnt-rely-on-luck-why-do-you/'
      },
      {
        clicks: 8753,
        shares: 7125,
        title: 'Imagination by Gravity4',
        url: 'http://gravity4.com/blog/imagination-by-gravity4/'
      },
      {
        clicks: 33124,
        shares: 23675,
        title: 'iBeacon. Shop Smarter',
        url: 'http://gravity4.com/blog/ibeacon/'
      },
      {
        clicks: 3334,
        shares: 1675,
        title: 'Introducing, Gravity4 Labs.',
        url: 'http://gravity4.com/blog/g4labs/'
      },
      {
        clicks: 0,
        shares: 0,
        title: 'Opt-out',
        url: 'http://gravity4.com/opt-out/'
      }]
  );

  //Retrieving event_url_all data for site 2 report
  $httpBackend.whenGET(
    getDigestQuery(2),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [{
      clicks: 343,
      shares: 343,
      title: 'Contact',
      url: 'http://demo.com/contact/'
    },
      {
        clicks: 234,
        shares: 345,
        title: 'Team',
        url: 'http://demo.com/team/'
      },
      {
        clicks: 34,
        shares: 75,
        title: 'Labs',
        url: 'http://demo.com/labs/'
      },
      {
        clicks: 633,
        shares: 467,
        title: 'Pricing',
        url: 'http://demo.com/pricing/'
      },
      {
        clicks: 34,
        shares: 675,
        title: 'Product',
        url: 'http://demo.com/product/'
      },
      {
        clicks: 34,
        shares: 75,
        title: 'Vision',
        url: 'http://demo.com/vision/'
      },
      {
        clicks: 834,
        shares: 275,
        title: 'Title 1',
        url: 'http://demo.com/blog/title1/'
      },
      {
        clicks: 34,
        shares: 12,
        title: 'Tile 2',
        url: 'http://demo.com/blog/title2/'
      },
      {
        clicks: 53,
        shares: 25,
        title: 'Title 3',
        url: 'http://demo.com/blog/title3/'
      },
      {
        clicks: 3324,
        shares: 2375,
        title: 'Title 4',
        url: 'http://demo.com/blog/title4/'
      },
      {
        clicks: 334,
        shares: 675,
        title: 'Title 5',
        url: 'http://demo.com/blog/title4/'
      },
      {
        clicks: 0,
        shares: 0,
        title: 'Opt-out',
        url: 'http://demo.com/opt-out/'
      }]
  );

  //Retrieving referring_searches data for site 1 report
  $httpBackend.whenGET(
    getDigestQuery(1),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {searches: 58, query: 'Development'},
      {searches: 11273, query: 'Interactive agency'},
      {searches: 3235, query: 'Carrer in IT'},
      {searches: 612, query: 'Coding service'},
      {searches: 23, query: 'Software House'},
      {searches: 725, query: 'Programming'},
      {searches: 8236, query: 'PHP Developer'},
      {searches: 826, query: 'SEO'},
      {searches: 269, query: 'UX Design'},
      {searches: 1252, query: 'Continuos integration'}
    ]
  );

  //Retrieving referring_searches data for site 2 report
  $httpBackend.whenGET(
    getDigestQuery(2),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {searches: 581, query: 'Development'},
      {searches: 1273, query: 'Interactive agency'},
      {searches: 335, query: 'Carrer in IT'},
      {searches: 1612, query: 'Coding service'},
      {searches: 223, query: 'Software House'},
      {searches: 75, query: 'Programming'},
      {searches: 836, query: 'PHP Developer'},
      {searches: 8426, query: 'SEO'},
      {searches: 2619, query: 'UX Design'},
      {searches: 12, query: 'Continuos integration'}
    ]
  );

  //Retrieving copied_keywords data for site 1 report
  $httpBackend.whenGET(
    getDigestQuery(1),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {times: 58, keywords: 'Development'},
      {times: 11273, keywords: 'Interactive agency'},
      {times: 3235, keywords: 'Carrer in IT'},
      {times: 612, keywords: 'Coding service'},
      {times: 23, keywords: 'Software House'},
      {times: 725, keywords: 'Programming'},
      {times: 8236, keywords: 'PHP Developer'},
      {times: 826, keywords: 'SEO'},
      {times: 269, keywords: 'UX Design'},
      {times: 1252, keywords: 'Continuos integration'}
    ]
  );

  //Retrieving copied_keywords data for site 2 report
  $httpBackend.whenGET(
    getDigestQuery(2),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {times: 581, keywords: 'Development'},
      {times: 1273, keywords: 'Interactive agency'},
      {times: 335, keywords: 'Carrer in IT'},
      {times: 1612, keywords: 'Coding service'},
      {times: 223, keywords: 'Software House'},
      {times: 75, keywords: 'Programming'},
      {times: 836, keywords: 'PHP Developer'},
      {times: 8426, keywords: 'SEO'},
      {times: 2619, keywords: 'UX Design'},
      {times: 12, keywords: 'Continuos integration'}
    ]
  );

  //Retrieving referring_domains data for site 1 report
  $httpBackend.whenGET(
    getDigestQuery(1),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {
        shares: 58,
        url: 'http://addnow.com/2014/09/piwik-piwik-pro-trustradius-buyers-guide/'
      },
      {
        shares: 11273,
        url: 'http://addnow.com/2014/10/clearcode-featured-agency-post/'
      },
      {
        shares: 3235,
        url: 'http://addnow.com/2getCompleteQuery014/07/target-engaged-customers/'
      },
      {
        shares: 612,
        url: 'http://addnow.com/2014/07/rejoiner-ecommerce-solution-cart-abandonment/'
      },
      {
        shares: 23,
        url: 'http://addnow.com/2014/08/hire-right-app-developers/'
      },
      {
        shares: 725,
        url: 'http://addnow.com/2014/12/agile-vs-waterfall-method/'
      },
      {
        shares: 8236,
        url: 'http://addnow.com/2014/12/importance-of-branding-ux-ui-software-development/'
      },
      {
        shares: 826,
        url: 'http://addnow.com/2014/10/programmers/'
      },
      {
        shares: 269,
        url: 'http://addnow.com/2014/10/hiring-process/'
      },
      {
        shares: 1252,
        url: 'http://addnow.com/2014/09/computers/'
      }
    ]
  );

  //Retrieving referring_domains data for site 2 report
  $httpBackend.whenGET(
    getDigestQuery(2),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    [
      {
        shares: 581,
        url: 'http://addnow.com/2014/09/piwik-piwik-pro-trustradius-buyers-guide/'
      },
      {
        shares: 1273,
        url: 'http://addnow.com/2014/10/clearcode-featured-agency-post/'
      },
      {
        shares: 335,
        url: 'http://addnow.com/2014/07/target-engaged-customers/'
      },
      {
        shares: 1612,
        url: 'http://addnow.com/2014/07/rejoiner-ecommerce-solution-cart-abandonment/'
      },
      {
        shares: 223,
        url: 'http://addnow.com/2014/08/hire-right-app-developers/'
      },
      {
        shares: 75,
        url: 'http://addnow.com/2014/12/agile-vs-waterfall-method/'
      },
      {
        shares: 836,
        url: 'http://addnow.com/2014/12/importance-of-branding-ux-ui-software-development/'
      },
      {
        shares: 8426,
        url: 'http://addnow.com/2014/10/programmers/'
      },
      {
        shares: 2619,
        url: 'http://addnow.com/2014/10/hiring-process/'
      },
      {
        shares: 12,
        url: 'http://addnow.com/2014/09/computers/'
      }
    ]
  );

  $httpBackend.whenGET(
    backendApi + 'account',
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      email: 'test@test.pl',
      offset: 60,
      has_analytics: false
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 60,
      old_password: '1234'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      old_password: ['Password is incorrect']
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 60,
      old_password: '1234',
      password: '123'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    400,
    {
      old_password: ['Password is incorrect'],
      password: ['Ensure this field has at least 4 characters.']
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 61,
      old_password: '123qwe',
      password: '1234',
      email: 'test@test.com',
      has_analytics: true
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 61,
      email: 'test@test.com',
      has_analytics: true
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 0,
      old_password: '123qwe',
      email: 'test@test.com'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 0,
      email: 'test@test.com',
      has_analytics: false
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 60,
      old_password: '123qwe',
      email: 'test@test.com'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 60,
      email: 'test@test.com',
      has_analytics: false
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 0,
      old_password: '123qwe',
      password: '1234',
      email: 'test@test.com'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 0,
      email: 'test@test.com',
      has_analytics: false
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 0,
      old_password: '123qwe'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 0,
      email: 'test@test.pl',
      has_analytics: false
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 60,
      old_password: '123qwe',
      password: '1234'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 60,
      email: 'test@test.pl',
      has_analytics: false
    }
  );
  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 60,
      old_password: '123qwe'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 60,
      email: 'test@test.pl',
      has_analytics: false
    }
  );
  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 0,
      old_password: '123qwe',
      password: '1234'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 0,
      email: 'test@test.pl',
      has_analytics: false
    }
  );
  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 0,
      old_password: '123qwe'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 0,
      email: 'test@test.pl',
      has_analytics: false
    }
  );

  $httpBackend.whenGET(/.*/).passThrough();
  $httpBackend.whenPOST(/.*/).passThrough();
  $httpBackend.whenPUT(/.*/).passThrough();
  $httpBackend.whenDELETE(/.*/).passThrough();
  $httpBackend.whenPATCH(/.*/).passThrough();

  // widget's settings
  // todo: move to widget tests
  $httpBackend.whenGET(
    widgetPrefix + 's'
  ).respond(
    400,
    'missing site id'
  );

  $httpBackend.whenGET(
    widgetPrefix + 's?idsite=1'
  ).respond(
    200,
    {
      hash_id: '1:04Q7fqXxgLx5HMtyPnXI8AWqDNY',
      uuid: '0lhaDqJIEeSXTwAWPpvNAw',
      follow: {
        text: ''
      },
      sharing: {
        byHash: false,
        copyPaste: false,
        hasShortUrls: true
      },
      widget_configurations: [
        {
          id: 1,
          name: 'default',
          orientation: 'horizontal',
          button_style: 'icon',
          button_size: 'medium',
          counter_position: 'right',
          type: 'sharing-buttons',
          is_active: true,
          buttons: [
            {
              service: 'facebook',
              isExtraButton: false,
              text: 'Facebook',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            },
            {
              service: 'twitter',
              isExtraButton: false,
              text: 'Twitter',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            }
          ],
          vanity_domain: ''
        },
        {
          id: 2,
          name: 'custom widget config',
          orientation: 'vertical',
          button_style: 'label',
          button_size: 'small',
          counter_position: 'top',
          type: 'sharing-buttons',
          is_active: true,
          buttons: [
            {
              service: 'googlePlus',
              isExtraButton: false,
              text: 'Google+',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            },
            {
              service: 'linkedin',
              isExtraButton: false,
              text: 'LinkedIn',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            },
            {
              service: 'facebook',
              isExtraButton: false,
              text: 'Facebook',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            }
          ],
          vanity_domain: ''
        },
        {
          id: 3,
          name: 'newsletter widget',
          orientation: 'horizontal',
          button_style: 'label',
          button_size: 'small',
          counter_position: 'top',
          page_url: 'test page url',
          page_title: 'test',
          type: 'newsletter',
          is_active: true,
          buttons: [
            {
              service: 'facebook',
              isExtraButton: false,
              text: 'Facebook',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            },
            {
              service: 'twitter',
              isExtraButton: false,
              text: 'Twitter',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            }
          ],
          vanity_domain: ''
        }
      ]
    },
    undefined,
    undefined,
    function(status, data, headers, statusText) {
      if (typeof data.uuid === 'string') {
        data.uuid = '0lhaDqJIEeSXTwAWPpvNAw';
      }

      return [status, data, headers, statusText];
    }

  );

  $httpBackend.whenGET(
    widgetPrefix + 's?idsite=1%3A04Q7fqXxgLx5HMtyPnXI8AWqDNY'
  ).respond(
    200,
    {
      hash_id: '1:04Q7fqXxgLx5HMtyPnXI8AWqDNY',
      uuid: '0lhaDqJIEeSXTwAWPpvNAw',
      follow: {
        text: ''
      },
      sharing: {
        byHash: false,
        copyPaste: false,
        hasShortUrls: true
      },
      widget_configurations: [
        {
          id: 1,
          name: 'default',
          orientation: 'horizontal',
          button_style: 'icon',
          button_size: 'medium',
          counter_position: 'right',
          type: 'sharing-buttons',
          is_active: true,
          buttons: [
            {
              service: 'facebook',
              isExtraButton: false,
              text: 'Facebook',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            },
            {
              service: 'twitter',
              isExtraButton: false,
              text: 'Twitter',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            }
          ],
          vanity_domain: ''
        },
        {
          id: 2,
          name: 'custom widget config',
          orientation: 'vertical',
          button_style: 'label',
          button_size: 'small',
          counter_position: 'top',
          type: 'sharing-buttons',
          is_active: true,
          buttons: [
            {
              service: 'googlePlus',
              isExtraButton: false,
              text: 'Google+',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            },
            {
              service: 'linkedin',
              isExtraButton: false,
              text: 'LinkedIn',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            },
            {
              service: 'facebook',
              isExtraButton: false,
              text: 'Facebook',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            }
          ],
          vanity_domain: ''
        },
        {
          id: 3,
          name: 'newsletter widget',
          orientation: 'horizontal',
          button_style: 'label',
          button_size: 'small',
          counter_position: 'top',
          page_url: 'test page url',
          page_title: 'test',
          type: 'newsletter',
          is_active: true,
          buttons: [
            {
              service: 'facebook',
              isExtraButton: false,
              text: 'Facebook',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            },
            {
              service: 'twitter',
              isExtraButton: false,
              text: 'Twitter',
              is_short_link: true,
              has_counter: true,
              follow_url: ''
            }
          ],
          vanity_domain: ''
        }
      ]
    },
    undefined,
    undefined,
    function(status, data, headers, statusText) {
      if (typeof data.uuid === 'string') {
        data.uuid = '0lhaDqJIEeSXTwAWPpvNAw';
      }

      return [status, data, headers, statusText];
    }

  );

  $httpBackend.whenGET(
    widgetPrefix + 's?idsite=2'
  ).respond(
    200,
    {
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      uuid: '6QJECKJJEeSbYgAWPpvNAw',
      follow: {
        facebook: 'http://facebook.com/url',
        text: 'thank you msg'
      },
      sharing: {
        byHash: true,
        copyPaste: true,
        hasShortUrls: true
      },
      widget_configurations: [{
        id: 1,
        name: 'default',
        orientation: 'horizontal',
        button_size: 'medium',
        button_style: 'icon',
        counter_position: 'right',
        type: 'sharing-buttons',
        is_active: true,
        buttons: [
          {
            has_counter: true,
            service: 'facebook',
            isExtraButton: false,
            text: 'Facebook',
            is_short_link: true,
            follow_url: ''
          },
          {
            service: 'twitter',
            isExtraButton: false,
            text: 'Twitter',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          }
        ],
        vanity_domain: ''
      }]
    },
    undefined,
    undefined,
    function(status, data, headers, statusText) {
      if (typeof data.uuid === 'string') {
        data.uuid = '6QJECKJJEeSbYgAWPpvNAw';
      }

      return [status, data, headers, statusText];
    }

  );
  $httpBackend.whenGET(
    widgetPrefix + 's?idsite=2%3AFeEqS2xWiIPRf0YA5Z6v0ig2bkM'
  ).respond(
    200,
    {
      uuid: '6QJECKJJEeSbYgAWPpvNAw',
      hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
      follow: {
        facebook: 'http://facebook.com/url',
        text: 'thank you msg'
      },
      sharing: {
        byHash: true,
        copyPaste: true,
        hasShortUrls: true
      },
      widget_configurations: [{
        id: 1,
        name: 'default',
        orientation: 'horizontal',
        button_size: 'medium',
        button_style: 'icon',
        counter_position: 'right',
        is_active: true,
        type: 'sharing-buttons',
        buttons: [
          {
            service: 'facebook',
            isExtraButton: false,
            text: 'Facebook',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          },
          {
            service: 'twitter',
            isExtraButton: false,
            text: 'Twitter',
            is_short_link: true,
            has_counter: true,
            follow_url: ''
          }
        ],
        vanity_domain: ''
      }]
    },
    undefined,
    undefined,
    function(status, data, headers, statusText) {
      if (typeof data.uuid === 'string') {
        data.uuid = '6QJECKJJEeSbYgAWPpvNAw';
      }

      return [status, data, headers, statusText];
    }

  );

  $httpBackend.whenGET(
    widgetPrefix + 'e'
  ).respond(
    400,
    'missing site id'
  );

  $httpBackend.whenGET(
    widgetPrefix + 'e?idsite=1&e_c=share&e_n=http%3A%2F%2Ftest.com&e_a=facebook&e_t=sharing-buttons'
  ).respond(
    204,
    ''
  );

  $httpBackend.whenGET(

    // jscs:disable maximumLineLength
    widgetPrefix + 'e?idsite=1%3A04Q7fqXxgLx5HMtyPnXI8AWqDNY&e_c=share&e_n=http%3A%2F%2Ftest.com&e_a=facebook&e_t=sharing-buttons'

    // jscs:enable maximumLineLength
  ).respond(
    204,
    ''
  );

  // tracking events
  // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
}

// jscs:disable requireCamelCaseOrUpperCaseIdentifiers
angular.module('angulardashDev', ['ngMockE2E'])
  .config(['$httpProvider', configuration])

  //mock backend
  .run(['loginBackend', '$httpBackend', 'AppSettings', runHandler]);

angular.module('angulardash').requires.push('angulardashDev');
