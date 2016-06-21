var gulp = require('gulp'),
    sass = require('gulp-sass'),
    notify = require('gulp-notify'),
    browserSync = require('browser-sync'),
    imagemin = require('gulp-imagemin'),
    uglify = require('gulp-uglify'),
    autoprefixer = require('gulp-autoprefixer'),
    runSequence = require('run-sequence'),
    rename = require('gulp-rename'),
    pngquant = require('imagemin-pngquant');

// Task to compile SCSS
gulp.task('sass', function () {
  return gulp.src('./src/scss/**/*.scss')
    .pipe(sass({
      outputStyle: 'compressed',
      errLogToConsole: false,
    })
    .on("error", notify.onError(function(error) {
      return "Failed to Compile SCSS: " + error.message;
    })))
    .pipe(autoprefixer())
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('./css/'))
    .pipe(browserSync.stream())
    .pipe(notify("SCSS Compiled Successfully :)"));
});

// Task to Minify JS
gulp.task('compressjs', function() {
  return gulp.src(['./src/js/**/*.js'])
    .pipe(uglify())
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('./js/'));
});

// Minify Images
gulp.task('compImages', function() {
  return gulp.src('./src/img/**/*.png')
    .pipe(imagemin({
      progressive: true,
      svgoPlugins: [{removeViewBox: false}],
      use: [pngquant()]
    }))
    .pipe(gulp.dest('./img/'));
});

// BrowserSync Task (Live reload)
gulp.task('browserSync', function() {
    browserSync.init({
        proxy: "hodor.dev:3063"
    });
});

// Gulp Watch Task
gulp.task('watch', ['browserSync'], function () {
   gulp.watch('./src/scss/**/*.scss', ['sass']),
   gulp.watch('./src/js/**/*.js', ['compressjs']).on('change', browserSync.reload),
   gulp.watch('../templates/**/*.html').on('change', browserSync.reload);
});

// Gulp Default Task
gulp.task('default', ['watch']);

// Gulp Build Task
gulp.task('build', function() {
  runSequence('imagemin', 'compressjs');
});