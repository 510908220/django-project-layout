# -*- coding: utf-8 -*-
"""
任务调度器:调度job下面各个子任务
1. 普通任务是调用jenkins接口
2. 紧急任务是通过fabric在远程主机执行命令

"""

import time
import logging
import sys
import os
import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings
from userapps.api.models import SeriousHost, NormalHost, Job, Package
from userapps.api import jenk

logger = logging.getLogger("dispatcher")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def normal_host_process(host):
    logger.info("start process normal host %s, revision is %s",
                host.ip, host.revision)
    build_no = jenk.get_next_build_number(host.job.component, host.ip)
    logger.info("next build num is %s", build_no)

    # 创建一个jenkins job
    host.build_no = build_no
    status_code = jenk.create_job_on_host(
        host.job.component, host.ip, settings.TOKEN, host.revision)
    if 200 <= status_code < 300:
        host.status = NormalHost.Status.running
        host.save()
    else:
        host.status = NormalHost.Status.bad
        logger.error(u"{0}创建远程任务失败,错误码:{1}".format(host.ip, status_code))
        host.save()
        return

    # 等待jenkins job结束
    while 1:
        host_job_info = jenk.get_host_info(host.job.component, host.ip)
        logger.info("host_job_info is:%s", host_job_info)
        color = host_job_info['color']
        last_build = host_job_info['lastBuild']

        # 如果是第一次构建，lastBuild是为None, color为notbuilt
        if last_build is None:
            time.sleep(5)
            continue

        remote_build_no = host_job_info['lastBuild']['number']
        # 提示:
        # 开始这里使用if color in ["aborted", "red", "blue"]:来检测是否完成构建,
        # 这样做的问题是有可能构建还没开始，所以获取的上一次状态。
        # 检测的前提是构建已开始，可以根据lastBuild获取
        if remote_build_no == host.build_no and color in ["aborted", "red", "blue"]:
            host.status = color
            host.save()
            break
        logger.info(u"正在运行{0},颜色为:{1}".format(host.ip, color))
        time.sleep(5)

    logger.info("end process normal host")


def serious_host_process(host):
    logger.info("start process serious host %s, cmd is %s",
                host.ip, host.command)

    # 主机执行任务开始
    host.status = SeriousHost.Status.running
    host.save()

    log_path = os.path.join(BASE_DIR, "fabric", "serious_job.log")
    fab_cmd = "{fab} -f {fab_file_path} set_settings:{log_path},{key_filename},{ip} main:'{command}'".format(
        fab="fab",
        fab_file_path=os.path.join(BASE_DIR, "fabric", "serious_job_fab.py"),
        log_path=log_path,
        key_filename=os.path.join(BASE_DIR, "fabric", "id_rsa"),
        command=host.command,
        ip=host.ip
    )
    logger.info("fab_cmd is {0}".format(fab_cmd))
    p = subprocess.Popen(fab_cmd, shell=True)
    p.wait()

    # 主机执行任务完成
    host.status = SeriousHost.Status.finished
    with open(log_path) as f:
        host.result = f.read()
    host.save()

    logger.info("end process serious host %s, cmd is %s",
                host.ip, host.command)


def job_process(package):
    """
    例行包任务的处理，这里通过调用jenkins接口完成
    """
    logger.info("start process package:%s", package.version)

    new_jobs = package.jobs.filter(status=Job.Status.new)
    job_type = package.type
    for job in new_jobs:
        logger.info("start process normal job:%s", job)
        # 修改状态为正在处理
        job.status = Job.Status.running
        job.save()

        if job_type == Package.Type.normal:
            # 处理普通例行包任务
            new_hosts = NormalHost.objects.filter(status=NormalHost.Status.new)
            for host in new_hosts:
                try:
                    normal_host_process(host)
                except Exception, e:
                    logger.exception("普通升级{0}出错:{1}".format(host.ip, str(e)))
                    host.status = NormalHost.Status.bad
                    host.save()

        else:
            new_hosts = SeriousHost.objects.filter(
                status=SeriousHost.Status.new)
            for host in new_hosts:
                try:
                    serious_host_process(host)
                except Exception, e:
                    logger.exception("紧急升级{0}出错:{1}".format(host.ip, str(e)))
                    host.status = SeriousHost.Status.bad
                    host.save()

        # 修改状态为已完成
        job.status = Job.Status.finished
        job.save()
        logger.info("end process job:%s", job)

    logger.info("start process package:%s", package.version)


class Command(BaseCommand):
    help = '升级任务处理'

    def run(self):
        logger.info("start run")
        packages = Package.objects.all()
        for package in packages:
            job_process(package)
        logger.info("end run")

    def handle(self, *args, **options):
        while 1:
            try:
                time.sleep(15)
                self.run()
            except KeyboardInterrupt:
                logger.error("KeyboardInterrupt")
                sys.exit(0)
            except Exception, e:
                logger.error("Exception:%s" % e)
