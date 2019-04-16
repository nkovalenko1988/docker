#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import configparser


def load_conf():

    hostname = subprocess.check_output('hostname')
    environment = hostname.decode('utf-8').rstrip()
    config = configparser.ConfigParser()
    config.read('config.d/config-deploy')
    PROJECT_HOME = config.get(environment, 'PROJECT_HOME')
    WEBAPPS_DIR = config.get(environment, 'WEBAPPS_DIR')
    DEPLOY_DIR = config.get(environment, 'DEPLOY_DIR')
    BACKUPS_DIR = config.get(environment, 'BACKUPS_DIR')
    RELEASE_WARS = config.get(environment, 'RELEASE_WARS')
    FILE_LOG = config.get(environment, 'FILE_LOG')
    USER_GROUP = config.get(environment, 'USER_GROUP')

    return ({'PROJECT_HOME': PROJECT_HOME,
             'WEBAPPS_DIR': WEBAPPS_DIR,
             'DEPLOY_DIR': DEPLOY_DIR,
             'BACKUPS_DIR': BACKUPS_DIR,
             'RELEASE_WARS': RELEASE_WARS,
             'FILE_LOG': FILE_LOG,
             'USER_GROUP': USER_GROUP}
            )


