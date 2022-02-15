from flask import Flask, request, render_template

from utils import *

app = Flask(__name__)
PORT = 8888

@app.route('/') #设置路由
def handle():
    return  render_template('main.html')


if __name__ == '__main__':
    app.run(port=PORT)