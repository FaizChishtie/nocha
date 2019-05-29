# determine the os running & handle operations 
from src.logger import log
from sys import platform

# determine os
def os_det():
    return platform

def use(os):
    if platform == "linux" or platform == "linux2":
        return 'n'
    elif platform == "darwin":
        return 'n'
    elif platform == "win32":
        return 'nodist'