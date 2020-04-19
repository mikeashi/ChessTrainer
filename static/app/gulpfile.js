const gulp = require('gulp');
const source = require('vinyl-source-stream');
const watchify = require('watchify');
const browserify = require('browserify');
const tsify = require('tsify');

const browserifyOpts = (debug) => ({
  entries: ['src/app.ts'],
  debug: debug
});

const destination = () => gulp.dest('../js');

const dev = () => browserify(browserifyOpts(true))
    .plugin(tsify)
    .bundle()
    .pipe(source('app.js'))
    .pipe(destination());

const watch = () => {

  const bundle = () => bundler
      .bundle()
      .on('error', error => logger.error(colors.red(error.message)))
      .pipe(source('app.js'))
      .pipe(destination());

  const bundler = watchify(
      browserify(Object.assign({}, watchify.args, browserifyOpts(true)))
          .plugin(tsify)
  ).on('update', bundle);

  return bundle();
};

gulp.task('dev', dev);
gulp.task('default', watch);
