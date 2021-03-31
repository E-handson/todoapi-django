# settings/production.py

from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['django.e-watanabe.tk']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DJANGO_DATABASES_NAME'),
        'USER': os.environ.get('DJANGO_DATABASES_USER'),
        'PASSWORD': os.environ.get('DJANGO_DATABASES_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DATABASES_HOST'),
        'POST': os.environ.get('DJANGO_DATABASES_PORT'),
    }
}