from fabric.api import *
from fabric.colors import *


########################
## Basic Config
########################
DBK_USER = 'doubankong'
DBK_REPO_NAME = 'doubankong/'
DBK_GIT = 'git://github.com/kylewu/doubankong.git'

DBK_HOME = '/srv/code/'

DBK_GROUP = DBK_USER
DBK_REPO_DIR = DBK_HOME + DBK_REPO_NAME
DBK_STATIC_DIR = DBK_HOME + 'static/'

########################
## Local Commands
########################


def dbk():
    local('./manage.py runserver')


def sh():
    local('./manage.py shell')

########################
## Deploy Commands
########################


def create_user():
    '''
    create user for our project in server
    '''
    pass


def clone():
    with settings(warn_only=True):
        if run("test -d %s" % DBK_HOME).failed:
            # create DBK_HOME if it's not existed
            sudo('mkdir -p %s' % DBK_HOME)
            sudo('chown -R %s:%s %s' % (DBK_USER, DBK_GROUP, DBK_HOME))

            # clone repo
            with cd(DBK_HOME):
                sudo("git clone %s" % DBK_GIT, user=DBK_USER)
        else:
            # get the latest code
            with cd(DBK_REPO_DIR):
                sudo("git pull", user=DBK_USER)


def deploy():
    with cd(DBK_REPO_DIR):
        sudo('git pull', user=DBK_USER)
