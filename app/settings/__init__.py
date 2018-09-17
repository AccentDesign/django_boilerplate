from .base import *
from .helpers import env_mode


# environment settings

try:
    if env_mode() == 'DEV':
        from .dev import *
    elif env_mode() == 'STAGING':
        from .staging import *
        from .sentry import *
    else:
        from .sentry import *
except ImportError:
    pass
