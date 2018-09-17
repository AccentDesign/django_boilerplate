from django.conf import settings

from storages.backends.s3boto3 import S3Boto3Storage


# Storage classes - see http://snippets.accentdesign.co.uk/pages/django-s3-private-and-public-images/


class S3PrivateStorage(S3Boto3Storage):
    """
    A storage class that forcefully removes the custom domain

    This will force the class to revert back to the default s3 way of generating the urls
    with the querystring auth.

    acl='private' will mark the files as private when saving meaning
    the they will return an AccessDenied without the querystring auth.
    """

    def __init__(self, acl='private', bucket=None, **settings):
        settings.update({'custom_domain': None})
        super().__init__(acl, bucket, **settings)


class S3PublicStorage(S3Boto3Storage):
    """ Just subclass or use original class """


class S3StaticStorage(S3Boto3Storage):
    """ Stores files with the path prefix STATICFILES_LOCATION """

    location = settings.STATICFILES_LOCATION
