# -*- coding: utf-8 -*-
"""
任务调度器:调度job下面各个子任务
1. 普通任务是调用jenkins接口
2. 紧急任务是通过fabric在远程主机执行命令

"""

import time
import logging
import sys
from django.core.management.base import BaseCommand
from django.conf import settings

logger = logging.getLogger("dispatcher")


class Command(BaseCommand):
    help = '自定义命令描述'

    def run(self):
        logger.info("start run")
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
