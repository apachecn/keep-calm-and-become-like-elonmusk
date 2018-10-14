"""
We can store browsers specific state in session ,
no matter how many browsers interact with our webapp,
each browsers server side data is managed for us by Flask whenever session is used
"""
from flask import Flask
bharathapp = Flask(__name__)

@bharathapp.route('/')
def hello() -> str:
    return "hello from bharaths web"

@bharathapp.route('/page1')
def page1() -> str:
    return "this is page1"

@bharathapp.route('/page2')
def page2() -> str:
    return "this is page2"

@bharathapp.route('/page3')
def page3() -> str:
    return "this is page3"


if __name__ == '__main__':
    bharathapp.run(debug=True)