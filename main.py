from flask import Flask, request, render_template

from utils import *

app = Flask(__name__)
PORT = 8888

@app.route('/') #设置路由
def handle():
    return  render_template('main.html')

@app.route('/c1')
def c1_handle():
    confirm, confirm_add, heal, dead = get_c1_data()
    return jsonify({ #构造字典并转成json对象
        'confirm': confirm,
        'confirm_add': confirm_add,
        'heal': heal,
        'dead': dead
    })



if __name__ == '__main__':
    app.run(port=PORT)