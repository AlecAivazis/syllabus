"""
Django settings for syllabus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u2me%mqm!-lo&9((-$_c3$+b0=ws&izb44x#=1faq-u+^sgilr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# django apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
# third party apps
THIRD_PARTY = (
    'django_extensions',
)

# syllabus is just a collection of apps... whoa... meta
SYLLABUS = (
    'syllabus.core',
    'syllabus.academia',
    'syllabus.classroom',
    'syllabus.messages',
    'syllabus.wishlist',
    'syllabus.socialservice',
)

# the url permissions of the various user groups (to be moved somewhere else)
PERMS = {
    'student': ['uploadify', 'gradebook', 'viewevent', 'calendar', 'calendarajax', 'admin','login', 'logout', 'viewclass', '', 'resources', 'myhomework','messageboard'],
    'teacher' : ['','viewevent','uploadify',  'login', 'logout', 'viewclass', 'resources', 'calendar', 'calendarajax', 'gradebook', 'messageboard'],
    'registrar' : ['','login', 'viewevent', 'uploadify', 'logout', 'viewclass', 'resources', 'registrar', 'messageboard']
}

# Application definition
INSTALLED_APPS = DJANGO_APPS +  THIRD_PARTY + SYLLABUS


# load the appropriate base user class
AUTH_USER_MODEL = 'core.SyllUser'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'syllabus.urls'

WSGI_APPLICATION = 'apache.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Resource settings

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'resources').replace('\\','/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

STATIC_DOC_ROOT = os.path.join(os.path.dirname(__file__), 'resources/').replace('\\','/')
STATIC_ADMIN_MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'Syllabus/media').replace('\\','/')

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static').replace('\\','/')
COMPRESS_URL = '/static/'
STATIC_URL = '/static/'

COMPRESS_PRECOMPILERS =(
    ('text/scss', 'sass {infile} > {outfile}'),
)

COMPRESS_ENABLED = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'resources/').replace('\\','/'),
)
