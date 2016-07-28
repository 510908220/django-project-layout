# -*- coding:utf-8 -*-
import logging
import os
from codecs import open
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.aggregates import Max
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Shop
from .serializers import ShopSerializer

logger = logging.getLogger("api")

# http://blog.jobbole.com/41233/


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    开始像POST之类的请求时可以的，后来应该是执行了migrate,创建了用户，然后执行POST之类的请求
    会出现'detail csrf failed csrf token missing or incorrect',这个解决方案是可行的的
    :http://stackoverflow.com/questions/30871033/django-rest-framework-remove-csrf
    后续得研究一下
    """

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class ShopList(APIView):
    """
    商店创建与获取
    """
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopDetail(APIView):
    """
    获取可用的项目列表
    """
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_shop(self, shop_id):
        try:
            shop = Shop.objects.get(pk=shop_id)
            return shop
        except Shop.DoesNotExist:
            return None

    def get(self, request, shop_id, format=None):
        """
        获取资源
        """
        shop = self.get_shop(shop_id)
        if not shop:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def put(self, request, shop_id, format=None):
        shop = self.get_shop(shop_id)
        if not shop:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, shop_id, format=None):
        shop = self.get_shop(shop_id)

        # 删除是等幕操作
        if shop:
            shop.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
