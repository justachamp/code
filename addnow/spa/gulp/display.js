'use strict';

var gulp = require('gulp');
var child;

gulp.task('xvfb-start', function(cb) {
  var headless = require('headless');
  var options = {
    display: {
      width: 1920, height: 1080, depth: 32
    }
  };

  headless(options, function(err, childProcess, servernum) {
    // childProcess is a ChildProcess, as returned from child_process.spawn()
    console.log('Xvfb display number: ', servernum);
    child = childProcess;
    console.log('Xvfb pid:', childProcess.pid);
    console.log('Error code: ', err);
    process.env.DISPLAY = ':' + servernum;
    cb();
  });
});

module.exports.killDisplayProcess = function() {
  console.log('Killing xvfb display...');
  if(child) {
    child.kill();
  }
};
