from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class S3StaticStorage(S3Boto3Storage):
    """Stores files with the path prefix STATICFILES_LOCATION"""

    location = settings.STATICFILES_LOCATION
