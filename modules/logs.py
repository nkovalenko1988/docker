#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import datetime
from classes.set_color import Color


def print_logs(VERSION_RELEASE, text_log):

    name_file_log = 'deploy-log_' + VERSION_RELEASE + '_' + str(datetime.date.today()) + '.txt'

    try:
        f = open('logs/' + name_file_log, 'x')
    except FileExistsError:
        f = open('logs/' + name_file_log, 'a')

    f.write(str(datetime.datetime.now()) + text_log)


