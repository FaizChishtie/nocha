from src.logger import log
import os, subprocess

# cmd methods

def executable(prog):
    return os.path.isfile(prog) and os.access(prog, os.X_OK)

def which(e):
    path, name = os.path.split(e)

    if path:
        if executable(e):
            return executable
    
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe = os.path.join(path, name)
            if executable(exe):
                return exe
    
    return None

def do_ext(command, _os): 
    log('Doing ~' + command)

    w32 = ''

    if _os == 'win32':
        w32 = 'cmd /c'

    os.system(w32 + command)