# -*- encoding:utf-8 - *-
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from .views import ShopList, ShopDetail

urlpatterns = [
    url(r'shops/', ShopList.as_view(), name='shop_list'),
    url(r'shops/(?P<pk>[0-9]+)/', ShopDetail.as_view(), name='shop_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
