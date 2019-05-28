import json, glob, re
from log import log

# gets and validates input based on validator output
# on None invalid
def get_input(message, validator):
    u_in = input(message)

    log('Validating ~' + u_in)

    if validator(u_in):
        log('\n~' + u_in + ' valid')
        return u_in
    
    log('Invalid input ~' + u_in + ' try again...')
    return get_input(message, validator)

# reads json file as package.json
# looks for dependencies for node version
def read_json(file):
    with open(file) as jfile:
        dep = json.load(jfile)
        return transform_dep_readable(dep['dependencies']['node'])

# looks for file in current directory
def find_file(file):
    return glob.glob('./' + file)

# find first digit and trim from there 
def transform_dep_readable(node_v):
    m = re.search('\d', node_v)
    return node_v[m.start()::]