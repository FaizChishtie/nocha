from log import log

# gets and validates input based on validator output
# on None invalid
def get_input(message, validator):
    u_in = input(message)

    log('Validating ~' + u_in)

    if validator(u_in):
        log('~' + u_in + ' valid')
        return u_in
    
    log('Invalid input ~' + u_in + ' try again...')
    get_input(message, validator)
