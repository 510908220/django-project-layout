# -*- coding: utf-8 -*-
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        "PASSWORD": "",
        'NAME': '',
        'TEST': {'CHARSET': 'UTF8'}
    }
}
