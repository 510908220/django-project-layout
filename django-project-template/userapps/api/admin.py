# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.contrib import admin
from models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    fieldsets = (
        ("基本信息", {'fields': ('name', )}),
        ("属性", {'fields': ('category', 'status')}),
    )

    list_display = ['name', 'category', 'status', 'created', ]
