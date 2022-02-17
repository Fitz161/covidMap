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

@app.route('/c2')
def c2_handle():
    result = []
    for item in get_c2_data():
        result.append({'name': item[0], 'value': item[1]})
    return jsonify({'keyData': result})



if __name__ == '__main__':
    app.run(port=PORT)