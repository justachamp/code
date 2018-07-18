'use strict';

var gulp = require('gulp');
var util = require('util');
var browserSync = require('browser-sync');
var historyApiFallback = require('connect-history-api-fallback');

function browserSyncInit(baseDir, files, browser) {
  browser = browser === undefined ? 'default' : browser;

  var routes = null;
  if (baseDir === 'src' || (util.isArray(baseDir) && baseDir.indexOf('src') !== -1)) {
    routes = {
      // Should be '/bower_components': '../bower_components'
      // Waiting for https://github.com/shakyShane/browser-sync/issues/308
      '/bower_components': 'bower_components'
    };
  }

  browserSync.instance = browserSync.init(files, {
    startPath: '/index.html',
    server: {
      baseDir: baseDir,
      middleware: [historyApiFallback()],
      routes: routes
    },
    browser: browser,
    notify: false
  });

}

gulp.task('serve', ['watch'], function() {
  browserSyncInit([
    'src',
    '.tmp'
  ], [
    '.tmp/app/**/*.css',
    'src/assets/images/**/*',
    'src/*.html',
    'src/app/**/*.html',
    'src/app/**/*.js'
  ]);
});

gulp.task('serve:dist', ['build'], function() {
  browserSyncInit('dist');
});

gulp.task('serve:e2e', function() {
  browserSyncInit(['src', '.tmp'], null);
});

gulp.task('serve:e2e-dist', ['watch'], function() {
  browserSyncInit('dist', null);
});
