'use strict';

var gulp = require('gulp');
var angularFilesort = require('./gulp-angular-filesort');
var $ = require('gulp-load-plugins')({
  pattern: ['gulp-*', 'main-bower-files', 'uglify-save-license', 'del'],
  lazy: true
});

function handleError(err) {
  console.error(err.toString());

  //jshint -W040
  this.emit('end');

  //jshint +W040
}

gulp.task('constants', function() {
  var environment = $.util.env.env || 'vagrant';
  console.log('Building application with profile:', environment);
  return gulp.src('src/app/configuration/configuration.json')
    .pipe($.ngConfig('angulardash.configuration', {
      environment: environment,
      createModule: true,
      wrap: true
    }))
    .pipe(gulp.dest('src/app/configuration/'));
});

gulp.task('styles', ['wiredep'],  function() {
  return $.rubySass('src/app/**/*.scss', {style: 'expanded', loadPath: ['bower_components/bootstrap-sass-official/assets/stylesheets/bootstrap'], compass: true})
    .on('error', handleError)
    .pipe($.autoprefixer('last 3 versions'))
    .pipe(gulp.dest('.tmp/app'))
    .pipe($.replace('../../../../common', '../../../common'))
    .pipe($.replace('../assets/', '../../src/assets/'))
    .pipe($.base64({ debug: true }))
    .pipe(gulp.dest('.tmp/app'))
    .pipe($.size());
});

gulp.task('styles-assets',  function() {
  return gulp.src('src/assets/stylesheets/*.css')
    .pipe(gulp.dest('dist/assets/stylesheets'))
    .pipe($.size());
});

gulp.task('code-analyze', function() {
  var stylish = require('gulp-jscs-stylish');
  var jshintConfig  = require('../../common/code-style/jshintrc.json');
  jshintConfig.lookup = false;
  return gulp.src(['src/app/**/*.js', '!src/app/configuration/configuration.js', '!src/app/e2e-*.js', 'gulp/**/*.js', 'src/test/**/*.js'])
    .pipe($.jscs({
      fix: true,
      configPath: '../common/code-style/.jscsrc'
    }))
    .pipe($.jscs.reporter())
    .pipe(stylish())
    .pipe($.jscs.reporter('fail'))
    .pipe($.jshint(jshintConfig))
    .pipe($.jshint.reporter('jshint-stylish'))
    .pipe($.jshint.reporter('fail'));
});

gulp.task('scripts', function() {
  return gulp.src('src/index.html')
    .pipe($.inject(gulp.src(['src/app/**/*.js', '!src/app/e2e*.js', '!src/app/**/*.spec.js'])
      .pipe(angularFilesort()), {
      relative: true,
      name: 'angular'
    })).pipe(gulp.dest('src')).pipe($.size());
});

gulp.task('partials', function() {
  return gulp.src('src/{app,assets}/**/*.html')
    .pipe($.minifyHtml({
      empty: true,
      spare: true,
      quotes: true
    }))
    .pipe($.ngHtml2js({
      moduleName: function(file) {
        var pathParts = file.path.split('/');
        var appFolderIndex = pathParts.indexOf('app');
        var moduleIndex = appFolderIndex + 1;
        if (pathParts[moduleIndex]) {
          return 'angulardash.' + pathParts[moduleIndex];
        } else {
          return 'angulardash';
        }
      }
    }))
    .pipe(gulp.dest('.tmp'))
    .pipe($.size());
});

gulp.task('html', ['styles', 'scripts', 'partials', 'code-analyze'], function() {
  var htmlFilter = $.filter('*.html');
  var jsFilter = $.filter('**/*.js');
  var cssFilter = $.filter('**/*.css');
  var assets;

  return gulp.src('src/index.html')
    .pipe($.inject(gulp.src('.tmp/{app,assets}/**/*.js'), {
      read: false,
      name: 'partials',
      addRootSlash: false,
      addPrefix: '../'
    }))
    .pipe($.preprocess())
    .pipe(assets = $.useref.assets())
    .pipe($.rev())
    .pipe(jsFilter)
    .pipe($.ngAnnotate())
    .pipe($.uglify({preserveComments: $.uglifySaveLicense}))
    .pipe(jsFilter.restore())
    .pipe(cssFilter)
    .pipe($.replace('bower_components/bootstrap-sass-official/assets/fonts/bootstrap', 'fonts'))
    .pipe($.replace('../fonts/fontawesome-webfont', '../assets/fonts/fontawesome-webfont'))
    .pipe($.csso())
    .pipe(cssFilter.restore())
    .pipe(assets.restore())
    .pipe($.useref())
    .pipe($.revReplace())
    .pipe(htmlFilter)
    .pipe($.minifyHtml({
      empty: true,
      spare: true,
      quotes: true
    }))
    .pipe(htmlFilter.restore())
    .pipe(gulp.dest('dist'))
    .pipe($.size());
});

gulp.task('images', function() {
  return gulp.src('src/assets/images/**/*')
    .pipe(gulp.dest('dist/assets/images'))
    .pipe($.size());
});

gulp.task('amchart-images', function() {
  return gulp.src('bower_components/amcharts/ammap/images/*')
    .pipe(gulp.dest('dist/assets/images/amcharts/ammap'))
    .pipe($.size());
});

gulp.task('bower-components-assets', function() {
  return gulp.src('bower_components/famfamfam-flags-sprite/src/flags-sprite.png')
    .pipe(gulp.dest('dist/styles'))
    .pipe($.size());
});

gulp.task('fonts', function() {
  return gulp.src($.mainBowerFiles())
    .pipe($.filter('**/*.{eot,svg,ttf,woff,woff2}'))
    .pipe($.flatten())
    .pipe(gulp.dest('dist/assets/fonts'))
    .pipe($.size());
});

gulp.task('fonts-assets', function() {
  return gulp.src('src/assets/**/*')
    .pipe($.filter('**/*.{eot,svg,ttf,woff,otf}'))
    .pipe($.rename(function(path) {
      var parts = path.dirname.split('/');
      parts.splice(0, 1);
      path.dirname = parts.join('/');
    }))
    .pipe(gulp.dest('dist/assets/fonts'))
    .pipe($.size());
});

gulp.task('misc', function() {
  return gulp.src(['src/**/*.ico', 'src/*.png'])
    .pipe(gulp.dest('dist'))
    .pipe($.size());
});

gulp.task('clean', function(done) {
  $.del(['.tmp', 'dist'], done);
});

gulp.task('build', ['html', 'amchart-images', 'images', 'bower-components-assets', 'fonts', 'fonts-assets', 'styles-assets', 'misc']);
