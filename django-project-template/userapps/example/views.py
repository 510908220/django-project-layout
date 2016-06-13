# -*- coding:utf-8 -*-

from django.shortcuts import render


# (TODO) 下面diamante有待整理
def index(request):
    return render(request, 'index.html', {})
