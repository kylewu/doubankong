from cuisine import *


def setup():
    group_ensure("doubankong")
    user_ensure("doubankong")
    group_user_ensure("doubankong", "doubankong")
