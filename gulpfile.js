/*
    ---------
    Task List
    ---------

    Name: default
    Purpose: everything

    Name: bootstrap_css + bootstrap4_css
    Purpose: build and prefix bootstrap css 

    Name: bootstrap_compress + bootstrap4_compress
    Purpose: minify bootstrap css 

    Name: bootstrap_fonts
    Purpose: Copies bootstrap fonts to dist folder

    Name: bootstrap_js + bootstrap4_js
    Purpose: Copies bootstrap js to dist folder

    Name: style_css
    Purpose: builds and autoprefix site css

    Name: style_compress
    Purpose: minifys site css

    Name: style_css_min
    Purpose: runs style_css and style_compress

    Name: style_watch
    Purpose: watches for changes to any .scss file in any folder within the src/style 
    directory then runs style_css_min

*/

var $ = require('gulp-load-plugins')();
var gulp = require('gulp');
var prefixer = require('autoprefixer');
var runSequence = require('run-sequence');

var config = {
    assetsDir: './static/assets',
    bootstrapDir: './node_modules/bootstrap-sass',
    bootstrap4Dir: './node_modules/bootstrap',
    publicDir: './static/dist',
    scssDir: './static/scss',
    tetherDir: './node_modules/tether'
};


/*
 * Bootstrap 3
 */
gulp.task('bootstrap_css', function() {
    return gulp.src(config.scssDir + '/bootstrap/bootstrap.scss')
        .pipe($.sourcemaps.init())
        .pipe($.sass({includePaths: [config.bootstrapDir + '/assets/stylesheets']}))
        .pipe($.postcss([prefixer({browsers: ['last 1 version']})]))
        .pipe($.sourcemaps.write())
        .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task('bootstrap_compress', function () {
    return gulp.src(config.publicDir + '/css/bootstrap.css')
        .pipe($.cssmin())
        .pipe($.rename({suffix: '.min'}))
        .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task( 'bootstrap_css_min', ['bootstrap_css'], function (cb) {
    runSequence(['bootstrap_compress'], cb );
});

gulp.task('bootstrap_fonts', function() {
    return gulp.src(config.bootstrapDir + '/assets/fonts/bootstrap/*')
        .pipe(gulp.dest(config.publicDir + '/fonts'));
});

gulp.task('bootstrap_js', function() {
    return gulp.src(config.bootstrapDir + '/assets/javascripts/*.js')
        .pipe(gulp.dest(config.publicDir + '/js'));
});


/*
 * Bootstrap 4
 */
gulp.task('bootstrap4_css', function() {
    return gulp.src(config.scssDir + '/bootstrap4/bootstrap.scss')
        .pipe($.sourcemaps.init())
        .pipe($.sass({includePaths: [config.bootstrap4Dir + '/scss']}))
        .pipe($.postcss([prefixer({browsers: ['last 1 version']})]))
        .pipe($.sourcemaps.write())
        .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task('bootstrap4_compress', function () {
    return gulp.src(config.publicDir + '/css/bootstrap.css')
        .pipe($.cssmin())
        .pipe($.rename({suffix: '.min'}))
        .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task( 'bootstrap4_css_min', ['bootstrap4_css'], function (cb) {
    runSequence(['bootstrap4_compress'], cb );
});

gulp.task('bootstrap4_js', function() {
    return gulp.src(
        [
            config.bootstrap4Dir + '/dist/js/bootstrap*.js',
            config.tetherDir + '/dist/js/*.js'
        ])
        .pipe(gulp.dest(config.publicDir + '/js'));
});


/*
 * Site
 */
gulp.task('style_css', function() {
    return gulp.src(config.scssDir + '/style/style.scss')
        .pipe($.sourcemaps.init())
        .pipe($.sass({}))
        .pipe($.postcss([prefixer({browsers: ['last 1 version']})]))
        .pipe($.sourcemaps.write())
        .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task('style_compress', function () {
    return gulp.src(config.publicDir + '/css/style.css')
        .pipe($.cssmin())
        .pipe($.rename({suffix: '.min'}))
        .pipe(gulp.dest(config.publicDir + '/css'));
});

gulp.task( 'style_css_min', function(cb) {
    runSequence('style_css', 'style_compress', cb);
});


/*
 * Global
 */
gulp.task('style_watch', ['style_css_min'], function (){
    gulp.watch(
        [
            config.scssDir + '/style/*.scss',
            config.scssDir + '/style/**/*.scss'
        ],
        ['style_css_min']);
});

gulp.task('default', function (cb) {
    runSequence([
        //'bootstrap_css_min',
        //'bootstrap_fonts',
        //'bootstrap_js',
        'bootstrap4_css_min',
        'bootstrap4_js',
        'style_css_min'],
        cb
    );
});