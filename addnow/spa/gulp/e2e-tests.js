'use strict';

var gulp = require('gulp');
var gulpsync = require('gulp-sync')(gulp);
var $ = require('gulp-load-plugins')();
var browserSync = require('browser-sync');
var display = require('./display');
var counter = 0;
var fkill = require('fkill');
var psList = require('ps-list');
var protractorTests = [
  'protractor-chrome'

  //05-19-2015: Uncomment when this is fixed: https://github.com/angular/protractor/issues/1734
  //'protractor-firefox'
];

function browserStop() {
  counter += 1;
  if (counter >= protractorTests.length) {
    browserSync.exit();
  }
}

//clean all hung processes valuable for tests
gulp.task('cleanup-processes', function(done) {
  var processNames = ['chrome', 'chromedriver', 'gulp', 'xdg-open'];
  var filtered;
  psList().then(function(data) {
    console.log('All processes', data);
    filtered = data.filter(function(item) {
      return (processNames.indexOf(item.name) >= 0) && process.pid !== item.pid;
    });

    console.log('Processes to kill: ', filtered);
    var pids = filtered.map(function(item) {
      return item.pid;
    });

    console.log('Killing pids...', pids);
    fkill(pids).then(done).catch(function(e) {
      console.log(e);
      done();
    });
  });

});

// jscs:disable requireCamelCaseOrUpperCaseIdentifiers
// Downloads the selenium webdriver
gulp.task('webdriver-update', $.protractor.webdriver_update);

gulp.task('webdriver-standalone', $.protractor.webdriver_standalone);

// jscs:enable requireCamelCaseOrUpperCaseIdentifiers
gulp.task('protractor-chrome', ['webdriver-update', 'wiredep'], function(done) {
  var testFiles = [];
  if ($.util.env.spec !== undefined) {
    testFiles = $.util.env.spec.split(',');
  } else {
    testFiles.push('test/e2e/**/*.spec.js');
  }

  var targetEnv = $.util.env.target || 'vagrant';
  console.log('Target environment for testing:', targetEnv);
  gulp.src(testFiles)
    .pipe($.protractor.protractor({
      configFile: 'test/protractor_chrome.conf.js',
      args: ['--params.target=' + targetEnv]
    }))
    .on('error', function(err) {
      console.error('Protractor Error: ' + err);
      browserStop();
      display.killDisplayProcess();
      done();
    })
    .on('end', function() {
      console.error('Tests are finished.');

      // Close browser sync server
      browserStop();
      display.killDisplayProcess();
      done();
    });
});

gulp.task('protractor-firefox', ['webdriver-update', 'wiredep'], function(done) {
  var testFiles = [];
  if ($.util.env.spec !== undefined) {
    testFiles = $.util.env.spec.split(',');
  } else {
    testFiles.push('test/e2e/**/signin-*.js');
  }

  var targetEnv = $.util.env.target || 'vagrant';
  console.log('Target environment for testing:', targetEnv);
  gulp.src(testFiles)
    .pipe($.protractor.protractor({
      configFile: 'test/protractor_chrome.conf.js',
      args: ['--params.target=' + targetEnv]
    }))
    .on('error', function(err) {
      console.error('Protractor Error: ' + err);

      // Make sure failed tests cause gulp to exit non-zero
      console.error(err);
      browserStop();
      display.killDisplayProcess();
      done();
    })
    .on('end', function() {
      console.error('Tests are finished.');

      // Close browser sync server
      browserStop();
      display.killDisplayProcess();
      done();
    });
});

gulp.task('protractor-only', protractorTests);

//Concurrent browser tests return inconsistent results
// gulp.task('protractor', ['serve:e2e', 'protractor-only']);

gulp.task('protractor', gulpsync.sync(['serve:e2e', 'constants', [protractorTests]]), function() {
});

gulp.task('protractor-headless', gulpsync.sync(['constants', 'xvfb-start', 'serve:e2e', [protractorTests]]), function() {
});

gulp.task('protractor:src', ['serve:e2e', 'protractor-only']);
gulp.task('protractor:dist', ['serve:e2e-dist', 'protractor-only']);
