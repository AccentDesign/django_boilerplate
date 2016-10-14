import os
import sys


# project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def dev_mode():
    """
    Check if we want to be in dev mode, this will be used to pull in dev settings overrides.

    :return bool:
    """
    return os.environ.get('DEV_MODE') is not None


def show_toolbar(request):
    """
    Force debug toolbar due to issue inside docker from external to container.

    Additionally we dont want this to be true if we are running tests locally in docker
    as this is not an accurate reflection of the live codebase.

    :param request:
    :return bool:
    """
    if sys.argv[1:2] == ['test']:
        return False
    return True
