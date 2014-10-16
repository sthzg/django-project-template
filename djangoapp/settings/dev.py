# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .base import *
from .utils import get_env_variable


SECRET_KEY = get_env_variable('DJ_##PROJECT##_DEV_SECRET_KEY')
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../public/static')

MEDIA_ROOT = os.path.join(BASE_DIR, '../public/media')
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DJ_##PROJECT##_DEV_DB_NAME'),
        'USER': get_env_variable('DJ_##PROJECT##_DEV_DB_USER'),
        'PASS': get_env_variable('DJ_##PROJECT##_DEV_DB_PASS'),
        'HOST': '',
        'PORT': ''}}

SERVER_EMAIL = get_env_variable('DJ_##PROJECT##_DEV_SERVER_EMAIL')
EMAIL_BACKEND = get_env_variable('DJ_##PROJECT##_DEV_EMAIL_BACKEND')
EMAIL_HOST = get_env_variable('DJ_##PROJECT##_DEV_EMAIL_HOST')
EMAIL_PORT = get_env_variable('DJ_##PROJECT##_DEV_EMAIL_PORT')
EMAIL_HOST_USER = get_env_variable('DJ_##PROJECT##_DEV_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('DJ_##PROJECT##_DEV_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = get_env_variable('DJ_##PROJECT##_DEV_EMAIL_USE_TLS')