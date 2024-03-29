from os import environ

from .base import INSTALLED_APPS, MIDDLEWARE

# Security

DEBUG = True


# debug toolbar

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_COLLAPSED": True,
    "SHOW_TOOLBAR_CALLBACK": "app.settings.helpers.show_toolbar",
}

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


# database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": environ.get("RDS_HOSTNAME"),
        "PORT": environ.get("RDS_PORT"),
        "NAME": environ.get("RDS_DB_NAME"),
        "USER": environ.get("RDS_USERNAME"),
        "PASSWORD": environ.get("RDS_PASSWORD"),
    }
}


# auth

AUTH_PASSWORD_VALIDATORS = []


# static

STATICFILES_STORAGE = "app.storages.LocalStaticStorage"


# files

DEFAULT_FILE_STORAGE = "app.storages.LocalFileStorage"
