from src.logger import log
from src.cmd import which, do_ext
from src.nochaio import get_input, read_json, find_file
from src.ospe import os_det, use
from . import __version__ as version

# use log for loggable

VERSION_NUMBER = version

DEPENDENCIES = { 'win32': [ 'nodist' ], 'darwin': [ 'n' ], 'linux': [ 'n' ], 'linux2': [ 'n' ] }

PACKAGE_JSON_EXISTS = False

NODE_VERSION_SPECIFIED = None

OPERATING_SYSTEM = None

COMMAND = None

# main routine
def main():
    print('\n\n\nWelcome to nocha v' + VERSION_NUMBER)

    log('\nDetecting OS')
    
    OPERATING_SYSTEM = os_det()
    log('\t~' + OPERATING_SYSTEM + ' detected...')

    COMMAND = use(OPERATING_SYSTEM)
    log('\nUsing ~\'' + COMMAND + '\'')

    if not test_dep(OPERATING_SYSTEM):
        input('Press any key to exit...')
        exit(1)

    pkg = 'package.json'

    PACKAGE_JSON_EXISTS = m_find_json(pkg)

    skip_m_in = False

    if PACKAGE_JSON_EXISTS:
        skip_m_in = read_pkg(pkg)

    if not skip_m_in:
        m_input(OPERATING_SYSTEM)

    print('\nnocha completed...')

    u_in = get_input('Start nocha again? (y)es/(n)o ~', vald_y_n)

    if (u_in == 'y'):
        m_input(OPERATING_SYSTEM)

# functors

# check s/i input valid
def vald_in_opt(u_in):
    if (u_in == 's' or u_in == 'i' or u_in=='u'):
        return True
    return False

# valid yes or no
def vald_y_n(u_in):
    if (u_in == 'y' or u_in=='n'):
        return True
    return False

# todo
def vald_pch(u_in):
    return True

# sub routines

#TODO CLEAN SUBS

# main input
def m_input(os):
    print('\n\n\nCurrent versions of node installed:')
    if os == 'win32':
        do_ext('nodist ls', os)
    else:
        do_ext('n ls', os)
    
    u_in = get_input('\n\n\nSelect: \n\t(s)wap node version\n\t(i)nstall node version\n\t(u)ninstall node version ~', vald_in_opt)
   
    if(u_in == 's'):
        swap(None, os)
    
    elif(u_in == 'i'):
        install(os)

    elif(u_in == 'u'):
        uninstall(os)

# swaps version
def swap(version_spec=None, os='win32'):
    if version_spec != None:
        log('Swapping node version to ~' + version_spec)
    else:
        print('\n\nSwap current node version')
        version_spec = get_input('Enter the version of node you\'d like to swap to ~', vald_pch)
    if os == 'win32':
        do_ext('nodist ' + version_spec, os)
        log('\nMatching npm version')
        do_ext('nodist npm match', os)
    else:
        do_ext('n use ' + version_spec, os)
    log('Swapped node version ~' + version_spec)
    

# install
def install(os):
    print('\n\nInstall new node version')
    u_in = get_input('Enter the version of node you\'d like to install ~', vald_pch)
    if os == 'win32':
        do_ext('nodist + ' + u_in, os)
    else:
        do_ext('n ' + u_in, os)
    log('Installed node version ~' + u_in)

# uninstall
def uninstall(os):
    print('\n\nInstall new node version')
    u_in = get_input('Enter the version of node you\'d like to remove ~', vald_pch)
    if os == 'win32':
        do_ext('nodist - ' + u_in, os)
    else:
        do_ext('n rm ' + u_in, os)
    log('Uninstalled node version ~' + u_in)

# find json file
def m_find_json(pkg):
    log('\n\nSearching for ~\'' + pkg + '\' file...')

    tmp = 'not found'
    found = False

    if find_file(pkg):
        tmp = 'found'
        found = True

    log('\t~\'' + pkg + '\' ' + tmp + ' ...')
    return found

# tests dependencies 
#TODO MOVE TO OSPE
def test_dep(OPERATING_SYSTEM):
    print('\n\nTesting dependencies...')
    for dep in DEPENDENCIES[OPERATING_SYSTEM]:
        test = which(dep)
        if(test == None):
            log('Dependency ' + dep  + ' not installed...\nPlease install and try again...')
            return False
        log(dep + ' OK')
    log('Dependencies OK')
    return True

def read_pkg(pkg):
    log('Reading ~\'' + pkg + '\'...')
    NODE_VERSION_SPECIFIED = read_json(pkg)

    if(NODE_VERSION_SPECIFIED):
        log('\nFound ~' + NODE_VERSION_SPECIFIED)
        swap(NODE_VERSION_SPECIFIED)
        return True
    
    return False

if __name__ == "__main__":
    main()
