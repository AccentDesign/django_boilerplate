from django.contrib.staticfiles.storage import StaticFilesStorage
from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage


class LocalFileStorage(FileSystemStorage):
    pass


class LocalStaticStorage(StaticFilesStorage):
    pass


class S3Storage(S3Boto3Storage):
    pass
