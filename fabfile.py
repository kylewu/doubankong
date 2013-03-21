from fabric.api import *
from fabric.colors import *


########################
## Server Config
########################
DBK_HOME = '/srv/code/'
DBK_REPO_NAME = 'doubankong'
DBK_GIT = 'git://github.com/kylewu/doubankong.git'
DBK_USER = 'doubankong'
DBK_GROUP = 'doubankong'

DBK_REPO_FOLDER = DBK_HOME + DBK_REPO_NAME

########################
## Local Commands
########################


def dbk():
    local('./manage.py runserver')

########################
## Deploy Commands
########################


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
            with cd(DBK_REPO_FOLDER):
                sudo("git pull", user=DBK_USER)


def deploy():
    with cd(DBK_REPO_FOLDER):
        sudo('git pull', user=DBK_USER)
