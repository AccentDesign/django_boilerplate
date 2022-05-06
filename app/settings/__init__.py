from .base import *
from .helpers import env_mode

# environment settings

try:
    if env_mode() == "DEV":
        from .dev import *
except ImportError:
    pass
