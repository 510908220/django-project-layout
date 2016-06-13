from django.contrib import admin
from models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'status', 'console')
        }),
    )

    list_display = ['name', 'id', 'created', 'finished', 'status']
