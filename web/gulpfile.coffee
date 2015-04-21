# the gulpfile for the frontend of syllabus

# enable strict mode
'use strict'

# imports
browserify = require('browserify')
watchify = require('watchify')
gulp = require('gulp')
rename = require('gulp-rename')
source = require('vinyl-source-stream')
sourcemaps = require('gulp-sourcemaps')
assign = require('lodash.assign')
gutil = require('gulp-util')
buffer = require('vinyl-buffer')
babelify = require('babelify')
livereload = require('gulp-livereload')

# browserify configuration
customOpts = 
    entries: './src/app.js'
    debug: true
opts = assign({}, watchify.args, customOpts)

# create a watchify wrapper around browserify
b = watchify(browserify(opts).transform(babelify))
# if browserify needs to log something then do so through the terminal
b.on('log', gutil.log)


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
gulp.task('scripts', scripts)
gulp.task('watch', watch)

# the default task for gulp
gulp.task('default', ['watch'])



# end of file