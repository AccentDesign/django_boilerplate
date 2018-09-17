from os import environ
import sys

from .base import (
    INSTALLED_APPS,
    MIDDLEWARE
)


# Security

DEBUG = True


# debug toolbar

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_COLLAPSED': True,
    'SHOW_TOOLBAR_CALLBACK': 'app.settings.helpers.show_toolbar',
}

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': environ.get('RDS_HOSTNAME'),
        'PORT': environ.get('RDS_PORT'),
        'NAME': environ.get('RDS_DB_NAME'),
        'USER': environ.get('RDS_USERNAME'),
        'PASSWORD': environ.get('RDS_PASSWORD'),
    }
}


# auth

AUTH_PASSWORD_VALIDATORS = []


# static

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# files

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detail': {
            'format': (
                '%(levelname)s %(asctime)s %(pathname)s:%(lineno)s '
                '[%(funcName)s] %(message)s')
        }
    },
    'handlers': {
        'stdout': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'detail',
            'stream': sys.stdout
        }
    },
    'loggers': {
        'django': {
            'handlers': ['stdout'],
            'level': 'INFO',
        }
    }
}
