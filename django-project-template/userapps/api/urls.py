# -*- encoding:utf-8 - *-
from rest_framework.urlpatterns import format_suffix_patterns
from smarturls import surl

from .views import *

from rest_framework.urlpatterns import format_suffix_patterns
from smarturls import surl

from .views import ShopList, ShopDetail

urlpatterns = [
    surl(r'/shops/', ShopList.as_view(), name='shop_list'),
    surl(r'/shops/<username:shop_id>', ShopDetail.as_view(), name='shop_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
