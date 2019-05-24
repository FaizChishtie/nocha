from log import log
from cmd import which, do_ext
from nochaio import get_input

# use log for loggable

VERSION_NUMBER = '0.1.0'

DEPENDENCIES = [ 'nodist' , 'choco' ]

# main routine
def main():
    print('Welcome to nocha v' + VERSION_NUMBER)
    test_dep()

    print('\n\nCurrent versions of node installed:')
    do_ext('nodist ls')
    u_in = get_input('Select: \n\t(s)wap node version\n\t(i)nstall node version\n\t(u)ninstall node version ~', vald_in_opt)
   
    if(u_in == 's'):
        swap()
    
    elif(u_in == 'i'):
        install()

    elif(u_in == 'u'):
        uninstall()
    
    print('nocha completed...')

    u_in = get_input('Start nocha again? (y)es/(n)o ~', vald_y_n)

    if (u_in == 'y'):
        main()

# functors

# check s/i input valid
def vald_in_opt(u_in):
    if (u_in == 's' or u_in == 'i'):
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

# swap
def swap():
    print('\n\nSwap current node version')
    u_in = get_input('Enter the version of node you\'d like to swap to ~', vald_pch)
    do_ext('nodist ' + u_in)
    log('Swapped node version ~' + u_in)

# install
def install():
    print('\n\nInstall new node version')
    u_in = get_input('Enter the version of node you\'d like to install ~', vald_pch)
    do_ext('nodist +' + u_in)
    log('Installed node version ~' + u_in)

# uninstall
def uninstall():
    print('\n\nInstall new node version')
    u_in = get_input('Enter the version of node you\'d like to remove ~', vald_pch)
    do_ext('nodist -' + u_in)
    log('Uninstalled node version ~' + u_in)

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



if __name__ == "__main__":
    main()