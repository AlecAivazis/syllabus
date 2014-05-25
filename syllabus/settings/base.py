"""
Django settings for syllabus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
ROOT = os.path.join(BASE_DIR, 'packages', 'syllabus')


# important folders

TEMPLATES = os.path.join(BASE_DIR, 'templates').replace('\\','/')
RESOURCES = os.path.join(BASE_DIR, 'resources').replace('\\','/')
STATIC = os.path.join(RESOURCES, 'static').replace('\\','/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u2me%mqm!-lo&9((-$_c3$+b0=ws&izb44x#=1faq-u+^sgilr'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

# the directories that contains my templates
TEMPLATE_DIRS = (
    TEMPLATES,
)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# django apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
)

# third party apps
THIRD_PARTY = (
    'django_extensions',
    'compressor',
    'rest_framework',
)

# Application definition
INSTALLED_APPS = DJANGO_APPS +  THIRD_PARTY 

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

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
MEDIA_ROOT = RESOURCES

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Static Files

STATIC_DOC_ROOT = RESOURCES
STATIC_ADMIN_MEDIA_ROOT = os.path.join(ROOT, 'Syllabus/media').replace('\\','/')

STATIC_ROOT = STATIC
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
