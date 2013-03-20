from fabric.api import local


########################
## Local Commands
########################

def dbk():
    local('./manage.py runserver')
