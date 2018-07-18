'use strict';

// jscs:disable requireCamelCaseOrUpperCaseIdentifiers

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
  var sites = {};
  var routing = {};
  var pages = [
    {label: 'clearcode.cc'},
    {label: 'piwik.pro'},
    {label: 'gravity4.com'}
  ];
  var backendApi = AppSettings.backendApi;
  var widgetPrefix = '/';
  var idExpr;

  function getNextSiteId(sites) {
    var size = 0;
    var key;
    for (key in sites) {
      size++;
    }

    return size + 1;
  }

  sites[1] = {
    address_bar_sharing: false,
    copy_paste_sharing: false,
    api_key: '1254856352048jwdf285',
    domain: 'test.pl.domain.com',
    id: 1,
    thank_you_message: '',
    widget_configurations: [],
    social_urls: []
  };
  sites[2] = {
    address_bar_sharing: true,
    copy_paste_sharing: true,
    api_key: '1shh463520sgjw2f28w',
    domain: 'test.pl.domain.with.social.urls.com',
    id: 2,
    thank_you_message: 'thank you msg',
    widget_configurations: [1],
    social_urls: [{
      id: 1,
      service: 'facebook',
      url: 'http://facebook.com/url'
    }]
  };

  idExpr = backendApi + 'sites/([0-9]+)';
  idExpr = new RegExp(idExpr.replace('/', '\\/'));
  routing.sites = {};
  routing.sites.get = idExpr;
  routing.sites.remove = idExpr;
  routing.sites.update = idExpr;
  routing.sites.list = backendApi + 'sites';
  routing.sites.create = routing.sites.list;

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

  function getAllReports(siteId) {
    return new RegExp(backendApi + 'digest\\?(begin_date=([0-9])+&)?(end_date=([0-9])+&)?site=' + siteId);
  }

  function getDayReports(siteId) {
    return new RegExp(backendApi +
      'digest\\?aggregation=day&(begin_date=([0-9])+&)?(end_date=([0-9])+&)?site=' + siteId);
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

  loginBackend.when(
    'POST',
    backendApi + 'tokens',
    {
      email: 'newUser@test.pl',
      password: 'new password'
    }
  ).respond(
    200,
    {
      token: '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4c'
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
      id: 4,
      email: 'newUser@test.pl'
    },
    undefined,
    undefined,
    function(status, data, headers, statusText) {
      data.token = '8c92a1ea7ee011e4ba898c89a5640f47';
      data.id = 2;
      return [status, data, headers, statusText];
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
      email: 'test@test.pl'
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

  // Get all widget configurations
  $httpBackend.whenPOST(
    backendApi + 'sites/1/widgets'

    //loginBackend.session('test@test.pl')
  ).respond(function(method, url, data) {
    var mockData = JSON.parse(data);

    // Create site without credentials
    if (mockData.name === '123') {
      return [401, {
        detail: 'Authentication credentials were not provided.'
      }, {}];
    }

    if (mockData.name === '124') {
      return [200, {}, {}];
    }
  });

  $httpBackend.whenPOST(
    backendApi + 'sites/1/widgets'

    //loginBackend.session('test@test.pl')
  ).respond(400, {
    name: [
      'This field may not be blank.1',
      'This field may not be blank.2'
    ],
    counter_position: [
      'This field may not be blank.11',
      'This field may not be blank.22'
    ],
    non_field_errors: [
      'User must be unique12',
      'User must be unique23'
    ]
  });

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
        media_url: '',
        page_url: '',
        page_title: '',
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
        ]
      },
      {
        id: 2,
        name: 'custom widget config',
        orientation: 'vertical',
        button_style: 'label',
        button_size: 'small',
        counter_position: 'top',
        media_url: '',
        page_url: '',
        page_title: '',
        type: 'sharing-buttons',
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
        ]
      },
      {
        id: 3,
        name: 'newsletter widget',
        orientation: 'horizontal',
        button_style: 'label',
        button_size: 'small',
        counter_position: 'top',
        media_url: 'test media url',
        page_url: 'test page url',
        page_title: 'test',
        type: 'newsletter',
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
        ]
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
      ]
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
      ]
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
      ]
    }
  );

  // Get all sites
  $httpBackend.whenGET(routing.sites.list).respond(
    function() {
      var list = [];
      var i;
      for (i = 1; i < getNextSiteId(sites); i++) {
        list.push(sites[i]);
      }

      return [200, list];
    }

  );

  // Get site
  $httpBackend.whenGET(
    routing.sites.get,
    loginBackend.session('test@test.pl')
  ).respond(
    function(method, url) {
      var mockId = url.match(routing.sites.get)[1];
      return [200, sites[mockId]];
    }

  );

  // DELETE site. FOR TESTING PURPOSE ONLY!!!!
  $httpBackend.whenDELETE(routing.sites.remove).respond(
    function(method, url) {
      var mockId = url.match(routing.sites.get)[1];
      delete sites[mockId];
      return [200];
    }

  );

  $httpBackend.whenPOST(routing.sites.create).respond(
    function(method, url, data, headers) {
      var mockId;
      var i;

      // Create site without credentials
      if (!headers) {
        return [401, {
          detail: 'Authentication credentials were not provided.'
        }];
      }

      // Create site: nested errors for social urls
      if (data.social_urls) {
        for (i = 0; i < data.social_urls.length; i++) {
          url = data.social_urls[i];
          if (!url.url || !url.service) {
            return [400,
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
              }];
          }
        }
      }

      mockId = getNextSiteId(sites);
      sites[mockId] = JSON.parse(data);
      sites[mockId].id = mockId;

      // Create site without social urls
      if (data.widget_configurations && !data.social_urls) {
        return [201, sites[mockId]];
      }

      return [200, sites[mockId]];
    }

  );

  // Update site address_bar_sharing
  $httpBackend.whenPATCH(routing.sites.update).respond(
    function(method, url, data) {
      var socialUrl;
      var mockId;
      var i;

      if (data.social_urls) {
        for (i = 0; i < data.social_urls.length; i++) {
          socialUrl = data.social_urls[i];
          if (socialUrl.service === 'google') {
            return [
              400,
              {
                social_urls:[{
                  service: ['"google" is not a valid choice.']
                }]
              }
            ];
          }
        }
      }

      mockId = url.match(routing.sites.update)[1];
      sites[mockId] = JSON.parse(data);
      sites[mockId].id = parseInt(mockId);
      return [200, sites[mockId]];
    }

  );

  //Retrieving data for site 1 report
  $httpBackend.whenGET(
    getAllReports(1),
    loginBackend.session('test@test.pl')
  ).respond(
    200,

    // jscs:disable maximumLineLength
    {
      cached: false,
      data: {
        eventsSummary: [
          {views: 0, follows: 0, copies: 0, shares: 10, date: '2015-04-22 00:00:00', clicks: 0},
          {views: 0, follows: 0, copies: 0, shares: 4, date: '2015-04-24 00:00:00', clicks: 6},
          {views: 0, follows: 0, copies: 0, shares: 48, date: '2015-04-27 00:00:00', clicks: 15},
          {views: 0, follows: 0, copies: 0, shares: 18, date: '2015-04-28 00:00:00', clicks: 8},
          {views: 0, follows: 0, copies: 0, shares: 2, date: '2015-04-29 00:00:00', clicks: 1},
          {views: 0, follows: 0, copies: 0, shares: 5, date: '2015-04-30 00:00:00', clicks: 5},
          {views: 0, follows: 2, copies: 4, shares: 25, date: '2015-05-13 00:00:00', clicks: 19},
          {views: 0, follows: 0, copies: 0, shares: 0, date: '2015-05-14 00:00:00', clicks: 1}
        ],
        referringDomains: [],
        searchEngines: [],
        searchTerms: [],
        sharesAndClicksByTool: [
          {sharesPercent: 71.0, clicksPercent: 21.0, clicks: 12, shares: 80, tool: 'sharing-buttons'},
          {sharesPercent: 28.0, clicksPercent: 78.0, clicks: 43, shares: 32, tool: 'address-bar'}
        ],
        topContentByClicks: [
          {clicksPercent: 62.0, clicks: 5, url: 'http://testing.addnow.com/demo/', title: ''},
          {clicksPercent: 25.0, clicks: 2, url: 'http://lardissone.tumblr.com/', title: ''},
          {clicksPercent: 12.0, clicks: 1, url: 'http://lardissone.tumblr.com/post/60134752371', title: ''},
          {clicksPercent: 0.0, clicks: 0, url: 'http://en.wikipedia.org/', title: ''}
        ],
        topContentByShares: [
          {sharesPercent: 55.0, shares: 5, url: 'http://testing.addnow.com/demo/', title: ''},
          {sharesPercent: 33.0, shares: 3, url: 'http://lardissone.tumblr.com/', title: ''},
          {sharesPercent: 11.0, shares: 1, url: 'http://en.wikipedia.org/', title: ''},
          {sharesPercent: 0.0, shares: 0, url: 'http://lardissone.tumblr.com/post/60134752371', title: ''}
        ],
        topCountries: [
          {country: 'AR', viralLift: 0, id: 'AR', shares: 58, clicks: 24},
          {country: 'US', viralLift: 0, id: 'US', shares: 28, clicks: 23},
          {country: 'PT', viralLift: 0, id: 'PT', shares: 24, clicks: 6},
          {country: 'UA', viralLift: 1, id: 'UA', shares: 2, clicks: 2}
        ],
        topSocialChannels: [
          {sharesPercent: 39.0, clicksPercent: 3.0, clicks: 2, shares: 44, source: 'sms'},
          {sharesPercent: 21.0, clicksPercent: 52.0, clicks: 29, shares: 24, source: 'instagram'},
          {sharesPercent: 13.0, clicksPercent: 16.0, clicks: 9, shares: 15, source: 'googlePlus'},
          {sharesPercent: 7.0, clicksPercent: 25.0, clicks: 14, shares: 8, source: 'darkSocial'},
          {sharesPercent: 6.0, clicksPercent: 0.0, clicks: 0, shares: 7, source: 'digg'},
          {sharesPercent: 5.0, clicksPercent: 0.0, clicks: 0, shares: 6, source: 'facebook'},
          {sharesPercent: 2.0, clicksPercent: 0.0, clicks: 0, shares: 3, source: 'twitter'},
          {sharesPercent: 1.0, clicksPercent: 0.0, clicks: 0, shares: 2, source: 'whatsapp'},
          {sharesPercent: 0.0, clicksPercent: 1.0, clicks: 1, shares: 1, source: 'linkedin'},
          {sharesPercent: 0.0, clicksPercent: 0.0, clicks: 0, shares: 1, source: 'pinterest'},
          {sharesPercent: 0.0, clicksPercent: 0.0, clicks: 0, shares: 1, source: 'delicious'}
        ],
        topFrequentlyCopied: [
          {copies: 2, keyword: 'dasasdads'}
        ],
        totalExternalShares: [
          {source: 'facebook', sharesPercent: 84, shares: 1772290},
          {source: 'googlePlus', sharesPercent: 13, shares: 277908},
          {source: 'pinterest', sharesPercent: 2, shares: 44412},
          {source: 'twitter', sharesPercent: 0, shares: 3871},
          {source: 'linkedin', sharesPercent: 0, shares: 2601}
        ]
      }
    }

    // jscs:enable maximumLineLength
  );

  //Retrieving day report data for site 2 report
  $httpBackend.whenGET(
    getDayReports(2),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      cached: false,
      query: {site: 2},
      data: {
        eventsSummary: [
          {follows: 0, copies: 0, date: '2015-03-02 00:00:00', shares: 0, clicks: 4},
          {follows: 0, copies: 0, date: '2015-03-04 00:00:00', shares: 0, clicks: 4},
          {follows: 0, copies: 0, date: '2015-03-06 00:00:00', shares: 0, clicks: 4},
          {follows: 0, copies: 0, date: '2015-03-07 00:00:00', shares: 0, clicks: 4},
          {follows: 0, copies: 0, date: '2015-03-09 00:00:00', shares: 4, clicks: 0},
          {follows: 0, copies: 0, date: '2015-03-11 00:00:00', shares: 0, clicks: 0},
          {follows: 0, copies: 0, date: '2015-03-12 00:00:00', shares: 4, clicks: 0},
          {follows: 0, copies: 0, date: '2015-03-14 00:00:00', shares: 4, clicks: 0},
          {follows: 0, copies: 0, date: '2015-03-15 00:00:00', shares: 4, clicks: 0}
        ],
        referringDomains: [
          {domain: 'gravity4.com', url: 'http://gravity4.com/blog/article/', count: 1}
        ],
        searchEngines: [
          {searchEngine: 'Bing', percentage: 100, count: 58754}
        ],
        searchTerms: [
          {searchTerm: 'test the bing', percentage: 75, count: 44066},
          {searchTerm: 'test the bing2', percentage: 24, count: 14688}
        ],
        sharesAndClicksByTool: [
          {sharesPercent: 33.0, clicksPercent: 14.0, clicks: 1, shares: 3, tool: 'address-bar'},
          {sharesPercent: 22.0, clicksPercent: 28.0, clicks: 2, shares: 2, tool: 'copy-paste'}
        ],
        topContentByClicks: [
          {clicksPercent: 16.0, clicks: 1, title: 'http://addnow.com/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://addnow.com/new/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://addnow.com/press/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://addnow.com/blog/article-1/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://blog.com/post-5/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://gravity4.com/press/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://addnow.com/blog/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://addnow.com/contact/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/blog/article-2/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/blog/article-5/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/contact/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/features/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/labs/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/product/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/vision/'}
        ],
        topContentByShares: [
          {sharesPercent: 11.0, shares: 1, title: 'http://addnow.com/contact/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://addnow.com/blog/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/blog/article-2/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/blog/article-5/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/contact/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/features/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/labs/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/product/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/vision/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://addnow.com/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://addnow.com/blog/article-1/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://addnow.com/new/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://addnow.com/press/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://blog.com/post-5/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://gravity4.com/press/'}
        ],
        topCountries: [
          {country: 'US', id: 'US', shares: 5, clicks: 4},
          {country: 'MX', id: 'MX', shares: 2, clicks: 0},
          {country: 'AR', id: 'AR', shares: 1, clicks: 1},
          {country: 'ES', id: 'ES', shares: 1, clicks: 0},
          {country: 'IN', id: 'IN', shares: 0, clicks: 1},
          {country: 'RU', id: 'RU', shares: 0, clicks: 1}
        ],
        topFrequentlyCopied: [
          {copies: 1, keyword: 'analytics'},
          {copies: 1, keyword: 'consulting'},
          {copies: 1, keyword: 'web development'}
        ],
        topSocialChannels: [
          {sharesPercent: 55.0, clicksPercent: 14.0, clicks: 1, shares: 5, source: 'twitter'},
          {sharesPercent: 44.0, clicksPercent: 42.0, clicks: 3, shares: 4, source: 'facebook'},
          {sharesPercent: 0.0, clicksPercent: 28.0, clicks: 2, shares: 0, source: 'googlePlus'},
          {sharesPercent: 0.0, clicksPercent: 14.0, clicks: 1, shares: 0, source: 'linkedin'}
        ],
        totalExternalShares: [
          {source: 'twitter', sharesPercent: 75, shares: 9},
          {source: 'facebook', sharesPercent: 25, shares: 3}
        ]
      }
    }
  );

  //Retrieving day report data for site 1 report
  $httpBackend.whenGET(
    getDayReports(1),
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      cached: false,
      query: {site: 1},
      data: {
        eventsSummary: [
          {follows: 0, copies: 0, date: '2015-03-02 00:00:00', shares: 0, clicks: 4},
          {follows: 0, copies: 0, date: '2015-03-04 00:00:00', shares: 0, clicks: 4},
          {follows: 0, copies: 0, date: '2015-03-06 00:00:00', shares: 0, clicks: 4},
          {follows: 0, copies: 0, date: '2015-03-07 00:00:00', shares: 0, clicks: 4},
          {follows: 0, copies: 0, date: '2015-03-09 00:00:00', shares: 4, clicks: 0},
          {follows: 0, copies: 0, date: '2015-03-11 00:00:00', shares: 0, clicks: 0},
          {follows: 0, copies: 0, date: '2015-03-12 00:00:00', shares: 4, clicks: 0},
          {follows: 0, copies: 0, date: '2015-03-14 00:00:00', shares: 4, clicks: 0},
          {follows: 0, copies: 0, date: '2015-03-15 00:00:00', shares: 4, clicks: 0}
        ],
        referringDomains: [
          {domain: 'gravity4.com', url: 'http://gravity4.com/blog/article/', count: 1}
        ],
        searchEngines: [
          {searchEngine: 'Bing', percentage: 100, count: 58754}
        ],
        searchTerms: [
          {searchTerm: 'test the bing', percentage: 75, count: 44066},
          {searchTerm: 'test the bing2', percentage: 24, count: 14688}
        ],
        sharesAndClicksByTool: [
          {sharesPercent: 33.0, clicksPercent: 14.0, clicks: 1, shares: 3, tool: 'address-bar'},
          {sharesPercent: 22.0, clicksPercent: 28.0, clicks: 2, shares: 2, tool: 'copy-paste'}
        ],
        topContentByClicks: [
          {clicksPercent: 16.0, clicks: 1, title: 'http://addnow.com/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://addnow.com/new/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://addnow.com/press/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://addnow.com/blog/article-1/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://blog.com/post-5/'},
          {clicksPercent: 16.0, clicks: 1, title: 'http://gravity4.com/press/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://addnow.com/blog/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://addnow.com/contact/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/blog/article-2/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/blog/article-5/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/contact/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/features/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/labs/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/product/'},
          {clicksPercent: 0.0, clicks: 0, title: 'http://gravity4.com/vision/'}
        ],
        topContentByShares: [
          {sharesPercent: 11.0, shares: 1, title: 'http://addnow.com/contact/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://addnow.com/blog/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/blog/article-2/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/blog/article-5/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/contact/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/features/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/labs/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/product/'},
          {sharesPercent: 11.0, shares: 1, title: 'http://gravity4.com/vision/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://addnow.com/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://addnow.com/blog/article-1/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://addnow.com/new/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://addnow.com/press/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://blog.com/post-5/'},
          {sharesPercent: 0.0, shares: 0, title: 'http://gravity4.com/press/'}
        ],
        topCountries: [
          {country: 'US', id: 'US', shares: 5, clicks: 4},
          {country: 'MX', id: 'MX', shares: 2, clicks: 0},
          {country: 'AR', id: 'AR', shares: 1, clicks: 1},
          {country: 'ES', id: 'ES', shares: 1, clicks: 0},
          {country: 'IN', id: 'IN', shares: 0, clicks: 1},
          {country: 'RU', id: 'RU', shares: 0, clicks: 1}
        ],
        topFrequentlyCopied: [
          {copies: 1, keyword: 'analytics'},
          {copies: 1, keyword: 'consulting'},
          {copies: 1, keyword: 'web development'}
        ],
        topSocialChannels: [
          {sharesPercent: 55.0, clicksPercent: 14.0, clicks: 1, shares: 5, source: 'twitter'},
          {sharesPercent: 44.0, clicksPercent: 42.0, clicks: 3, shares: 4, source: 'facebook'},
          {sharesPercent: 0.0, clicksPercent: 28.0, clicks: 2, shares: 0, source: 'googlePlus'},
          {sharesPercent: 0.0, clicksPercent: 14.0, clicks: 1, shares: 0, source: 'linkedin'}
        ],
        totalExternalShares: [
          {source: 'twitter', sharesPercent: 75, shares: 9},
          {source: 'facebook', sharesPercent: 25, shares: 3}
        ]
      }
    }
  );

  $httpBackend.whenGET(
    backendApi + 'account',
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      email: 'test@test.pl',
      offset: 60
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset:60,
      old_password: '1234',
      password: '1'
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
      offset: 60,
      old_password: '123qwe',
      password: '1234',
      email: 'test@test.com'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 60,
      email: 'test@test.com'
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 240
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 240,
      email: 'test@test.com'
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      old_password: '123qwe',
      password: '1234'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 60,
      email: 'test@test.com'
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 0,
      email: 'test@test.com'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 0,
      email: 'test@test.com'
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 60,
      email: 'test@test.com'
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 60,
      email: 'test@test.com'
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
      email: 'test@test.com'
    }
  );

  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 0
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 0,
      email: 'test@test.pl'
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
      email: 'test@test.pl'
    }
  );
  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 60
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 60,
      email: 'test@test.pl'
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
      email: 'test@test.pl'
    }
  );
  $httpBackend.whenPATCH(
    backendApi + 'account',
    {
      offset: 0
    },
    loginBackend.session('test@test.pl')
  ).respond(
    200,
    {
      offset: 0,
      email: 'test@test.pl'
    }
  );

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
      uuid: '0lhaDqJIEeSXTwAWPpvNAw',
      hash_id: '1',
      follow: {
        text: ''
      },
      sharing: {
        byHash: false,
        copyPaste: false
      }
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
      uuid: '6QJECKJJEeSbYgAWPpvNAw',
      hash_id: '2',
      follow: {
        facebook: 'http://facebook.com/url',
        text: 'sharing msg'
      },
      sharing: {
        byHash: true,
        copyPaste: true
      }
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

  // tracking events

  $httpBackend.whenGET(/.*/).passThrough();
  $httpBackend.whenPOST(/.*/).passThrough();
  $httpBackend.whenPUT(/.*/).passThrough();
  $httpBackend.whenDELETE(/.*/).passThrough();
  $httpBackend.whenPATCH(/.*/).passThrough();
}

angular.module('angulardashDev', ['ngMockE2E'])
  .config(['$httpProvider', configuration])

  //mock backend
  .run(['loginBackend', '$httpBackend', 'AppSettings', runHandler]);

angular.module('angulardash').requires.push('angulardashDev');

