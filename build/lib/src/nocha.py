from log import log
from cmd import which, do_ext
from nochaio import get_input, read_json, find_file
from . import __version__ as version

# use log for loggable

VERSION_NUMBER = version

DEPENDENCIES = [ 'nodist' ]

PACKAGE_JSON_EXISTS = False

NODE_VERSION_SPECIFIED = None

# main routine
def main():
    print('\n\n\nWelcome to nocha v' + VERSION_NUMBER)
    test_dep()

    pkg = 'package.json'
    
    PACKAGE_JSON_EXISTS = m_find_json(pkg)

    skip_m_in = False

    if PACKAGE_JSON_EXISTS:
        skip_m_in = read_pkg(pkg)

    if not skip_m_in:
        m_input()

    print('\nnocha completed...')

    u_in = get_input('Start nocha again? (y)es/(n)o ~', vald_y_n)

    if (u_in == 'y'):
        m_input()

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

# main input
def m_input():
    print('\n\n\nCurrent versions of node installed:')
    do_ext('nodist ls')
    u_in = get_input('\n\n\nSelect: \n\t(s)wap node version\n\t(i)nstall node version\n\t(u)ninstall node version ~', vald_in_opt)
   
    if(u_in == 's'):
        swap()
    
    elif(u_in == 'i'):
        install()

    elif(u_in == 'u'):
        uninstall()

# swaps version
def swap(version_spec=None):
    if version_spec != None:
        log('Swapping node version to ~' + version_spec)
    else:
        print('\n\nSwap current node version')
        version_spec = get_input('Enter the version of node you\'d like to swap to ~', vald_pch)
    do_ext('nodist ' + version_spec)
    log('Swapped node version ~' + version_spec)

# install
def install():
    print('\n\nInstall new node version')
    u_in = get_input('Enter the version of node you\'d like to install ~', vald_pch)
    do_ext('nodist + ' + u_in)
    log('Installed node version ~' + u_in)

# uninstall
def uninstall():
    print('\n\nInstall new node version')
    u_in = get_input('Enter the version of node you\'d like to remove ~', vald_pch)
    do_ext('nodist - ' + u_in)
    log('Uninstalled node version ~' + u_in)

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
def test_dep():
    print('\n\nTesting dependencies...')
    for dep in DEPENDENCIES:
        test = which(dep)
        if(test == None):
            log('Dependency ' + dep  + ' not installed...\nPlease install and try again...')
            return
        log(dep + ' OK')
    log('Dependencies OK')

def read_pkg(pkg):
    log('Reading ~\'' + pkg + '\'...')
    NODE_VERSION_SPECIFIED = read_json(pkg)

    if(NODE_VERSION_SPECIFIED):
        log('\nFound ~' + NODE_VERSION_SPECIFIED)
        swap(NODE_VERSION_SPECIFIED)
        return True
    
    return False

def run():
    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    run()
