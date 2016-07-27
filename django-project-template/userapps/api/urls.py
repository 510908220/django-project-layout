from rest_framework.urlpatterns import format_suffix_patterns
from smarturls import surl

from .views import *

from rest_framework.urlpatterns import format_suffix_patterns
from smarturls import surl

from .views import *

urlpatterns = [
    surl(r'/shops/', ShopView.as_view(), name='shop'),
    surl(r'/shops/<username:shop_id>', ShopItemView.as_view(), name='shop_item'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
