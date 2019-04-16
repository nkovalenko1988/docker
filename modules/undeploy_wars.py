#!/usr/bin/python3
# -*- coding: utf-8 -*-

import shutil
import datetime
from modules import tail_log
from classes.set_color import Color


def del_wars(list_war, WEBAPPS_DIR, FILE_LOG):
    if list_war != '':
        try:
            print(str(datetime.datetime.now()) + ' - Start undeploy %s .' % list_war)
            shutil.rmtree(WEBAPPS_DIR + "/" + list_war)
            tail_log.run_command(list_war, FILE_LOG, 'undeploy')
            print('\n' + Color.Cyan + str(datetime.datetime.now()) + ' - Undeploy %s завершен!' % list_war + Color.END)
        except FileNotFoundError:
            print(str(datetime.datetime.now()) + ' - %s not found' % str(list_war))
    else:
        print(str(datetime.datetime.now()) + ' - list_war is empty')
