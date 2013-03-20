from cuisine import *
import fabric

fabric.api.env.host = ['vps']


def setup():
    group_ensure("doubankong")
    user_ensure("doubankong")
    group_user_ensure("doubankong", "doubankong")
