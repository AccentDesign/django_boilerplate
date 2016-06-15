var $ = require('gulp-load-plugins')();
var gulp = require('gulp');
var less = require('gulp-less');
var rename = require("gulp-rename");
var runSequence = require('run-sequence');
var sass = require('gulp-sass');

var config = {
    assetsDir: './static/assets',
    bootstrapDir: './node_modules/bootstrap-sass',
    publicDir: './static/dist'
};

gulp.task('bootstrap_css', function() {
    return gulp.src('./static/src/bootstrap/bootstrap.scss')
    .pipe($.sourcemaps.init())
    .pipe(sass({
        includePaths: [config.bootstrapDir + '/assets/stylesheets']
    }))
    .pipe($.postcss([
        require('autoprefixer-core')({browsers: ['last 1 version']})
    ]))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task('bootstrap_compress', function () {
  return gulp.src('./static/dist/css/bootstrap.css')
    .pipe($.csso())
    .pipe($.rename({
        suffix: '.min'
    }))
    .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task('bootstrap_fonts', function() {
    return gulp.src(config.bootstrapDir + '/assets/fonts/bootstrap/*')
    .pipe(gulp.dest(config.publicDir + '/fonts'));
});

gulp.task('bootstrap_js', function() {
    return gulp.src(config.bootstrapDir + '/assets/javascripts/*.js')
    .pipe(gulp.dest(config.publicDir + '/js'));
});

gulp.task('style_css', function() {
    return gulp.src('./static/src/style/style.scss')
    .pipe($.sourcemaps.init())
    .pipe(sass({}))
    .pipe($.postcss([
        require('autoprefixer-core')({browsers: ['last 1 version']})
    ]))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task('style_compress', function () {
  return gulp.src('./static/dist/css/style.css')
    .pipe($.csso())
    .pipe($.rename({
        suffix: '.min'
    }))
    .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task('jquery', function() {
    return gulp.src('./node_modules/jquery/dist/**')
    .pipe(gulp.dest(config.publicDir + '/js'));
});

gulp.task('fa_fonts', function() {
    return gulp.src('./node_modules/font-awesome/fonts/**')
    .pipe(gulp.dest(config.publicDir + '/fonts'));
});

gulp.task('fa_css', function() {
    return gulp.src('./node_modules/font-awesome/css/**')
    .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task('default', ['bootstrap_css', 'style_css', 'fa_css'], function (cb) {
    runSequence([
        'bootstrap_compress',
        'bootstrap_fonts',
        'bootstrap_js',
        'style_compress',
        'fa_fonts',
        'jquery'],
        cb
    );
});