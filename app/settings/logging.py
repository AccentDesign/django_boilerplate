import sys


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
        },
        '': {
            'handlers': ['stdout'],
            'level': 'INFO',
        }
    }
}
