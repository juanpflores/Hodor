from adventures.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['.megacopa.com']

MEDIA_URL = '/'

MEDIA_ROOT = os.getenv('DJANGO_MEDIA_ROOT')

STATIC_ROOT = os.getenv('DJANGO_STATIC_ROOT')
