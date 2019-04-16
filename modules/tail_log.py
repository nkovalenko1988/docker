#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import shlex
import datetime
from classes.set_color import Color


def run_command(list_war, FILE_LOG, stage):
    if stage == 'undeploy':
        u_str_find = ' were unregistered'
        u_str_find2 = ' was unregistered'
    elif stage == 'deploy':
        d_str_find = ' are available for use'
        d_str_find2 = ' is available for use'
    process = subprocess.Popen(shlex.split('tail -f -n1 %s' % FILE_LOG), stdout=subprocess.PIPE)
    print(str(datetime.datetime.now()) + ' - Reading log %s \n' % FILE_LOG)

    while True:
        output = process.stdout.readline()

        if stage == 'undeploy':
            if list_war + u_str_find in str(output) or list_war + u_str_find2 in str(output):
                print(Color.Yellow + str(output.strip().decode('utf-8')) + Color.END)
                break
            elif output:
                print(output.strip().decode('utf-8'))
        elif stage == 'deploy':
            if list_war + d_str_find in str(output) or list_war + d_str_find2 in str(output):
                print(Color.Yellow + str(output.strip().decode('utf-8')) + Color.END)
                break
            elif output:
                print(output.strip().decode('utf-8'))

    rc = process.poll()
    return rc







