# settings/local.py

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your_secret_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_local',
        'USER': 'django_user',
        'PASSWORD': 'secret',
        'HOST': 'db',
        'PORT': 3306
    }
}