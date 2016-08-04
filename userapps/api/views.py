# -*- coding:utf-8 -*-
import logging
from rest_framework import generics
from .models import Shop
from .serializers import ShopSerializer

logger = logging.getLogger("api")

# http://blog.jobbole.com/41233/
# http://www.django-rest-framework.org/tutorial/3-class-based-views/


class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
