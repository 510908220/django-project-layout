# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    """
    主页,根据用户角色不同返回不同的页面.
    普通用户:index_client.html
    管理员:index_admin.html
    """
    return render(request, "index.html", {})
