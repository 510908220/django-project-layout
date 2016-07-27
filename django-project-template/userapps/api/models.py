# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time
from django.conf import settings
from django.db import models
from django.utils import timezone
from model_utils import Choices
import logging
g_logger = logging.getLogger("api")


class Shop(models.Model):
    # https://django-model-utils.readthedocs.io/en/latest/utilities.html#choices
    # 商店类型
     CATEGORY = Choices(
            ('H', 'Hardware'),
            ('F', 'FRUITS'),
            ('C', 'COUTURE'),
        )

    STATUS = Choices(
        (0, 'open', 'open'),
        (1, 'closed', 'closed')
     )

    class Meta:
        db_table = "shop"

    name = models.CharField(
        max_length=200, unique=True, blank=False, null=False)
    category = models.CharField(choices=CATEGORY, default=CATEGORY.FRUITS, max_length=20)
    status = models.IntegerField(choices=STATUS, default=STATUS.open)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
        
    @staticmethod
    def delete_shop(pk):
        pass

    @staticmethod
    def get_shop(pk):
        try:
            project = Shop.objects.get(pk=pk)
            return project
        except Shop.DoesNotExist:
            return None
    @staticmethod
    def update_shop(pk, params):
        Shop.objects.filter(**params)
        return True

    @staticmethod
    def create_shop(params):
        try:
            shop = Shop.objects.create(**params)
            return True, shop
        except Exception, e:
            return False, str(e)
