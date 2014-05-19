# import base settings
from .syllabus import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# add django_toolbar to installed apps
INSTALLED_APPS += ("debug_toolbar", )

# add the debug_toolbar middleware
MIDDLEWARE_CLASSES += \
              ("debug_toolbar.middleware.DebugToolbarMiddleware",)

# set db to local sqlite database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db',  'db.sqlite3'),
    }
}
