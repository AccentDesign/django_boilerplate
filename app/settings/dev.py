import os

from .base import (
    INSTALLED_APPS,
    MIDDLEWARE_CLASSES
)


# Security

DEBUG = True


# debug toolbar

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_COLLAPSED': True,
    'SHOW_TOOLBAR_CALLBACK': 'app.settings.helpers.show_toolbar',
}

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]


# database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('RDS_HOSTNAME'),
        'PORT': os.environ.get('RDS_PORT'),
        'NAME': os.environ.get('RDS_DB_NAME'),
        'USER': os.environ.get('RDS_USERNAME'),
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
    }
}


# auth

AUTH_PASSWORD_VALIDATORS = []


# files

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
