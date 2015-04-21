# the gulpfile for the frontend of syllabus

# enable strict mode
'use strict'

# imports
assign = require('lodash.assign')
babelify = require('babelify')
browserify = require('browserify')
buffer = require('vinyl-buffer')
gulp = require('gulp')
eslint = require('gulp-eslint')
gutil = require('gulp-util')
livereload = require('gulp-livereload')
source = require('vinyl-source-stream')
sourcemaps = require('gulp-sourcemaps')
watchify = require('watchify')

# browserify configuration
customOpts = 
    entries: './src/app.js'
    debug: true
opts = assign({}, watchify.args, customOpts)

# create a watchify wrapper around browserify
b = watchify(browserify(opts).transform(babelify))
# if browserify needs to log something then do so through the terminal
b.on('log', gutil.log)


# perform various linting techniques on the javascript files
lint = ->
    # look at all javascript files
    gulp.src('src/**/*.js')
        .pipe(eslint())
        .pipe(eslint.format())
        .pipe(eslint.failOnError())


# build the scripts necessary for the application
scripts = ->
    # bundle the application
    b.bundle()
    # call it app.js
    .pipe(source('app.js'))
    .pipe(buffer())
    .pipe(sourcemaps.init({ loadMaps: true }))
    .pipe(sourcemaps.write('./')) 
    # write the file to the assets directory
    .pipe(gulp.dest('./assets'))
    .pipe(livereload())


# watch for changes in the javascript application
watch = ->
    # start the livereload server
    livereload.listen();
    # when browserify needs to update then rerun the scripts
    b.on 'update', ->
        # tell the user we saw the change
        console.log 'rebuilding application...'
        # recompile the javascript
        scripts()

    # compile the scripts
    scripts()


# gulp tasks
gulp.task('lint', lint)
gulp.task('watch', watch)
gulp.task('scripts', ['lint'],  scripts)
gulp.task('default', ['watch'])


# end of file