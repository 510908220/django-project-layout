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


class ShopView(APIView):
    """
    开发者管理
    """
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response(ShopSerializer(shop, many=True).data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        创建新的资源
        """
        shop = Shop.create_shop(request.data)
        return Response(ShopSerializer(shop).data, status=status.HTTP_200_OK)


class ShopItemView(APIView):
    """
    获取可用的项目列表
    """
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, shop_id, format=None):
        """
        获取资源
        """
        shop = Shop.get_shop(shop_id)
        return Response(ShopSerializer(shop).data, status=status.HTTP_200_OK)

    def put(self, request, shop_id, format=None):
        """
        修改资源
        """
        shop = Shop.update_shop(shop_id, request.data)
        return Response(ShopSerializer(shop).data, status=status.HTTP_200_OK)

    def delete(self, request, shop_id, format=None):
        """
        删除资源
        """
        Shop.delete_shop(shop_id)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
