from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/re_direct')
def re_direct():
    return redirect('https://duckduckgo.com')


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s</h1>' % name

@app.route('/math')
def math():
    return 1/0

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)
