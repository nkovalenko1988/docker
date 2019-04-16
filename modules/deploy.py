#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import os
from modules import tail_log
from classes.set_color import Color


def deploy_wars(list_war, RELEASE_WARS, DEPLOY_DIR, USER_GROUP, FILE_LOG):
    print(str(datetime.datetime.now()) + ' - Start deploy %s' % list_war)
    os.system("bash -c 'cd %s/*/ ; chown %s:%s %s*; cp -p %s* %s'" % (RELEASE_WARS, USER_GROUP, USER_GROUP, list_war, list_war, DEPLOY_DIR))
    tail_log.run_command(list_war, FILE_LOG, 'deploy')
    print('\n' + Color.Cyan + str(datetime.datetime.now()) + ' - Деплой %s завершен!' % list_war + Color.END)
