# -*- coding:utf-8 -*-
import logging
from rest_framework import generics
from .models import Shop
from .serializers import ShopSerializer
from rest_framework import filters

logger = logging.getLogger("api")

# http://blog.jobbole.com/41233/
# http://www.django-rest-framework.org/tutorial/3-class-based-views/

# 实际queryset 只是用于获取列表,不影响创建


class ShopList(generics.ListCreateAPIView):
    """
    过滤和排序都有对应的filter_backend, 具体使用查看
    http://www.django-rest-framework.org/api-guide/filtering/#orderingfilter
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('name', 'category',)
    ordering_fields = ('name', 'category')
    ordering = ('name',)


class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
