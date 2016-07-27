# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from userapps.api.models import Package


@login_required
def index(request):
    """
    主页,根据用户角色不同返回不同的页面.
    普通用户:index_client.html
    管理员:index_admin.html
    """
    return render(request,
                  "helper/index_admin.html" if request.user.is_superuser else "helper/index_client.html",
                  {"nav_active": "index", "select_name": "主页"})


def project(request):
    """Dashboard page.
    """
    return render(request, "helper/project.html",
                  {"nav_active": "project", "select_name": "项目管理"})


def collect(request):
    """Dashboard page.
    """
    return render(request, "helper/collect.html",
                  {"nav_active": "collect", "select_name": "收集管理"})


def summary(request):
    """Charts page.
    """
    return render(request, "helper/summary.html",
                  {"nav_active": "summary", "select_name": "收集整理"})


def email(request):
    """Tables page.
    """
    return render(request, "helper/email.html",
                  {"nav_active": "email", "select_name": "邮件管理"})


def content(request):
    """Forms page.
    """
    return render(request, "helper/content.html",
                  {"nav_active": "content", "select_name": "提交内容管理"})


def commit(request):
    """Forms page.
    """
    return render(request, "helper/commit.html",
                  {"nav_active": "commit", "select_name": "提交管理"})


def upgrade(request):
    """
    升级页面,根据类型和版本返回普通包的升级页面或紧急包的升级页面
    """

    tp = request.GET.get("type", None)
    version = request.GET.get("version", None)

    bad_render = render(request, "helper/upgrade.html",
                        {"nav_active": "upgrade", "select_name": "升级"})

    if not (tp and version):
        return bad_render

    templates = {
        "normal": "helper/upgrade_normal.html",
        "serious": "helper/upgrade_serious.html"
    }

    package = Package.objects.filter(
        version__contains=version, type=tp).first()
    if not package:
        return bad_render

    return render(request, templates[tp],
                  {"nav_active": "upgrade", "select_name": "升级", "version": package.version})


def jenkins(request):
    return render(request, "helper/jenkins.html",
                  {"nav_active": "jenkins", "select_name": "jenkins配置"})


def shell(request):
    return render(request, "helper/shell.html",
                  {"nav_active": "shell", "select_name": "shell"})


def schedule(request):
    return render(request, "helper/schedule.html",
                  {"nav_active": "schedule", "select_name": "schedule"})


def publishing(request):
    return render(request, "helper/publishing.html",
                  {"nav_active": "publishing", "select_name": "publishing"})
