# -*- coding: utf-8 -*-

import sys
import os

from .base import *

DEBUG = True

INSTALLED_APPS += ('debug_toolbar', 'django_extensions',)

# jupyter参数
NOTEBOOK_ARGUMENTS = [
    '--ip', 'localhost',
    '--port', '9527',
    # '--notebook-dir', os.path.join(BASE_DIR, "jupyter")
]


LOG_DIR = os.path.join(BASE_DIR, "log")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, "default.log"),  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, "error.log"),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': False
        },
        'api': {
            'handlers': ['default', 'error'],
            'level': 'INFO',
            'propagate': False
        },
    }
}
