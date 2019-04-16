#!/usr/bin/python3

import os
import glob
import shutil
import datetime


class Color:
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Grey = '\033[90m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


"""Creating backup components from webapps"""
"""Creating directory for the backup"""


def copy_portlets(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            try:
                shutil.copytree(s, d, symlinks, ignore)
            except FileExistsError:
                pass
        else:
            try:
                shutil.copy2(s, d)
            except FileExistsError:
                pass


def start_backup(list_war, VERSION_RELEASE, WEBAPPS_DIR, BACKUPS_DIR):
    try:
        os.mkdir(BACKUPS_DIR + "/" + VERSION_RELEASE)
    except FileExistsError:
        pass

    """ Get the component component directory for the backup according to the list
        we plan for deployment of components
    """
    i = 0
    while i < len(list_war):
        try:
            os.mkdir(BACKUPS_DIR + "/" + VERSION_RELEASE + "/" + list_war[i])
        except FileExistsError:
            pass
        w = glob.glob(WEBAPPS_DIR + "/" + list_war[i] + "*")
        if not not w:
            copy_portlets(w[0], BACKUPS_DIR + "/" + VERSION_RELEASE + "/" + list_war[i])
        i += 1

    now = datetime.datetime.now()
    print('\n' + Color.Cyan + str(now) + " - Backup %s is done!" % str(VERSION_RELEASE) + Color.END)


