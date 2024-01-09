from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-yk7w%fr28ihj)h2rilfh@b7j=l@fa49__9op(=fi6ogqy#8d4a'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'itwins',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'P'
    }
}