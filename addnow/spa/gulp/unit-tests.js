'use strict';

var gulp = require('gulp');
var wiredep = require('wiredep');
var gulpsync = require('gulp-sync')(gulp);
var Server = require('karma').Server;
var path = require('path');
var display = require('./display');

gulp.task('test', ['constants'], function(done) {
  var bowerDeps = wiredep({
    directory: 'bower_components',
    exclude: ['bootstrap-sass-official'],
    dependencies: true,
    devDependencies: true
  });

  var testFiles = bowerDeps.js.concat([
    'src/app/account-settings/account-settings.js',
    'src/app/getstarted/getstarted.js',
    'src/app/common/common.js',
    'src/app/configuration/configuration.js',
    'src/app/transform-middleware/transform-middleware.js',
    'src/app/main/main.js',
    'src/app/user/user.js',
    'src/app/site/site.js',
    'src/app/widget/widget.js',
    'src/app/navbar/navbar.js',
    'src/app/index.js',
    'src/app/**/*.js',

    //include the directory where directive templates are stored.
    'src/app/widget/buttons/extendable-buttons.html',
    'src/app/site/charts/range-map.html',
    'src/app/widget/buttons/ordered-buttons.html'
  ]);
  var karmaServer = new Server({
    configFile: path.resolve('test/karma.conf.js'),
    singleRun: true,
    files: testFiles
  }, done);
  karmaServer.start();
  return karmaServer.on('run_complete', function(browsers, results) {
    console.log('Failed tests: ', results.failed);
    console.log('End of work. Stopping Xvfb...');
    display.killDisplayProcess();
  });
});

gulp.task('test-headless', gulpsync.sync(['xvfb-start', 'test']), function() {
});
