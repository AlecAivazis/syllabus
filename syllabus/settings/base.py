# -*- Python -*-
# -*- coding: utf-8 -*-
#
# alec aivazis
#
"""
Django settings for syllabus

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# python imports
import os
import syllabus

# folder definitions
BASE = os.path.abspath(os.path.join(syllabus.home, os.pardir))
# important folder definitions
TEMPLATES = os.path.join(BASE, 'syllabus', 'templates')
RESOURCES = os.path.join(BASE, 'syllabus', 'assets')
STATIC_DIR = os.path.join(BASE, 'static')
UPLOADS = os.path.join(STATIC_DIR, 'uploads')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vza&3phs^-et5-)$5&x(udtdub@r=4(z6xr6tetn##lu^%4b-h'

# WSGI_APPLICATION = 'apache.wsgi.application'

ALLOWED_HOSTS = ['*']

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# set the authentication model
AUTH_USER_MODEL = 'authentication.SyllabusUser'

# Application definition

django_apps = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

third_party_apps = (
    'compressor',
 )

syllabus_apps = (
    'syllabus.apps.authentication',
    'syllabus.apps.academia',
    'syllabus.apps.classroom',
    'syllabus.apps.grading',
    'syllabus.apps.metadata',
    'syllabus.apps.messaging',
    'syllabus.apps.requirements',
    'syllabus.apps.scheduling'
)

INSTALLED_APPS = syllabus_apps + third_party_apps + django_apps

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'syllabus.urls'

APPEND_SLASH = True


# Template configuration

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('pyjade.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ]
        },
    },
]


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR
MEDIA_ROOT = UPLOADS

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)



# django compressor settings

COMPRESS_OUTPUT_DIR = "cache"

stylus_conf = ('-u jeet -u axis -u rupture -I ' +
               os.path.join(RESOURCES,'styles') +' < {infile} > {outfile}')

COMPRESS_PRECOMPILERS = (
    # ('text/cjsx', 'cjsx-transform {infile} | coffee --compile --stdio -b'),
    ('text/coffeescript', 'coffee --compile --stdio -b'),
    # ('text/es6', 'babel {infile} -o {outfile}'),
    ('text/stylus', 'stylus '+ stylus_conf),
)

# end of file
