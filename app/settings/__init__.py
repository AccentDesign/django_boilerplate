from .base import *
from .helpers import env_mode
from .logging import *


# environment settings

try:
    if env_mode() == 'DEV':
        from .dev import *
    if env_mode() == 'STAGING':
        from .staging import *
except ImportError:
    pass
