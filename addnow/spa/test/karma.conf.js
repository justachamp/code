'use strict';

module.exports = function(config) {

  config.set({
    basePath: '../', //!\\ Ignored through gulp-karma //!\\

    files: [//!\\ Ignored through gulp-karma //!\\
    ],

    autoWatch: false,

    frameworks: ['jasmine'],

    browsers: ['Chrome'],

    plugins: [
      'karma-jasmine',
      'karma-coverage',
      'karma-chrome-launcher',
      'karma-firefox-launcher',
      'karma-junit-reporter',
      'karma-ng-html2js-preprocessor'
    ],

    reporters: ['progress', 'junit', 'coverage'],

    preprocessors: {
      '**/*.html': ['ng-html2js'],
      'src/**/!(appSettings|e2e-api-mocks|e2e-loginBackend|e2e-mocks|index).js': ['coverage']
    },

    ngHtml2JsPreprocessor: {
      stripPrefix: 'src/'
    },

    // optionally, configure the reporter
    coverageReporter: {
      type: 'html',
      dir: '../var/tests-spa-js/coverage/',
      watermarks: {
        statements: [50, 80],
        functions: [50, 80],
        branches: [50, 80],
        lines: [50, 80]
      }
    },

    // the default configuration
    junitReporter: {
      outputFile: '../var/tests-spa-js/unit-test-results.xml',
      suite: ''
    }
  });

};
