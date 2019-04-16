#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import subprocess
import shlex
from modules.logs import print_logs
from classes.set_color import Color


def start_backup(list_war, VERSION_RELEASE, WEBAPPS_DIR, BACKUPS_DIR):

    a = BACKUPS_DIR + '/' + VERSION_RELEASE

    subprocess.call(shlex.split('mkdir %s ' % a), stderr=subprocess.PIPE)

    i = 0
    while i < len(list_war):
        if list_war[i] != '':
            b = WEBAPPS_DIR + '/' + list_war[i]
            subprocess.call(shlex.split('cp -pr %s %s' % (b, a)))
            i += 1
        else:
            i += 1

    print('\n' + Color.Cyan + str(datetime.datetime.now()) + ' - Backup %s выполнен!' % str(VERSION_RELEASE) + Color.END)

    print_logs(VERSION_RELEASE, ' - Backup %s выполнен!\n' % str(VERSION_RELEASE))

