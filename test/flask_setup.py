#!/usr/bin/env python

import sys

def check_args():
    if len(sys.argv) < 2:
        self = sys.argv[0]
        options = """
%s [options]

options:

help
initialize
initcode
spinwebserver
""" % self

        print(options)
        sys.exit(1)

    else:
        return sys.argv[1]


def options(argv):
    try:
        if argv == 'help':
	    setup = """
%s [options]

options:

help
initialize
initcode
spinwebserver
""" % sys.argv[0]


        if argv == 'initialize':
            setup = """
Init commands:

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install flask
$ pip freeze

"""

        if argv == 'spinwebserver':
            setup = """
Development Web Server:

$ export FLASK_APP=[file.py]
$ flask run

-or-

Add on the end of the file:

if __name__ == '__main__':
    app.run()

Debug mode:

$ export FLASK_APP=[file.py]
$ export FLASK_DEBUG=1
$ flask run

-or-

if __name__ == '__main__':
    app.run(debug=True)

"""
        if argv == 'initcode':
            setup = """
Initialize flask:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Server started working on localhost:5000</h2>'

"""
        
        print(setup)
    
    except UnboundLocalError:
        print('Type help as argument for details')




if __name__ == '__main__':
    
    check_args()
    options(sys.argv[1])
    sys.exit(0)


