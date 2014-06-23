# this file holds the syllabus specific file settings
from .base import *

# add the neccessary apps
INSTALLED_APPS += (
    'syllabus.core',
    'syllabus.academia',
    'syllabus.classroom',
    'syllabus.messages',
    'syllabus.wishlist',
    'syllabus.socialservice',
)

MIDDLEWARE_CLASSES = ( 
    'syllabus.core.middlewares.UAC',
) + MIDDLEWARE_CLASSES

# the url permissions of the various user groups (to be moved somewhere else)
PERMS = {
    'student': ['uploadify', 'gradebook', 'viewevent', 'calendar', 'calendarajax', 'admin','login', 'logout', 'viewclass', '', 'resources', 'myhomework','messageboard'],
    'teacher' : ['','viewevent','uploadify',  'login', 'logout', 'viewclass', 'resources', 'calendar', 'calendarajax', 'gradebook', 'messageboard'],
    'registrar' : ['','login', 'viewevent', 'uploadify', 'logout', 'viewclass', 'resources', 'registrar', 'messageboard']
}

# set the authentication model
AUTH_USER_MODEL = 'core.SyllUser'
# set the url conf
ROOT_URLCONF = 'syllabus.urls'
# point to the wsgi app
WSGI_APPLICATION = 'apache.wsgi.application'


# Django compressor settings

STATICFILES_DIRS = (
    RESOURCES, 
)

COMPRESS_URL = '/static/'

COMPRESS_PRECOMPILERS =(
    ('text/scss', 'sass {infile} > {outfile}'),
    ('text/coffeescript', 'coffee --compile --stdio'),
)


COMPRESS_JS_COMPRESSOR = 'compressor.js.JsCompressor'
COMPRESS_CSS_COMPRESSOR = 'compressor.css.CssCompressor'

COMPRESS_ROOT = RESOURCES

COMPRESS_OUTPUT_DIR = 'static'

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']

COMPRESS_PARSER = 'compressor.parser.AutoSelectParser'

COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'

COMPRESS_VERBOSE = False

COMPRESS_ENABLED = False

