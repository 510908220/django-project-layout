# -*- coding: utf-8 -*-

from __future__ import unicode_literals
# from django.conf import settings
from django.db import models
from model_utils import Choices
import logging
g_logger = logging.getLogger("api")


class Shop(models.Model):
    # https://django-model-utils.readthedocs.io/en/latest/utilities.html#choices
    # 商店类型
    CATEGORY = Choices(
        ('hardware', 'hardware'),
        ('fruits', 'fruits'),
        ('couture', 'couture'),
    )

    STATUS = Choices(
        (0, 'open', 'open'),
        (1, 'closed', 'closed')
    )

    class Meta:
        db_table = "shop"

    name = models.CharField(
        max_length=200, unique=True, blank=False, null=False)
    category = models.CharField(
        choices=CATEGORY, default=CATEGORY.fruits, max_length=20)
    status = models.IntegerField(choices=STATUS, default=STATUS.open)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
