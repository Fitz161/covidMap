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


@app.route('/l1')
def l1_handle():
    data:tuple = get_l1_data()
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for da, co, su, he, de in data:
        day.append(da.strftime('%m-%d')) #da为datetime类型
        confirm.append(co)
        suspect.append(su)
        heal.append(he)
        dead.append(de)
    return jsonify({
        'day': day,
        'confirm': confirm,
        'suspect': suspect,
        'heal': heal,
        'dead': dead
    })


@app.route('/l2')
def l2_handle():
    data:tuple = get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for da, ca, sa in data:
        day.append(da.strftime('%m-%d')) #da为datetime类型
        confirm_add.append(ca)
        suspect_add.append(sa)
    return jsonify({
        'day': day,
        'confirm_add': confirm_add,
        'suspect_add': suspect_add,
    })

@app.route('/r1')
def r1_handle():
    data = get_r1_data()
    province, confirm_add = [], []
    for pro, con in data:
        province.append(pro)
        confirm_add.append(con)
    return jsonify({
        'province': province,
        'confirm_add': confirm_add
    })

@app.route('/r2')
def r2_handle():
    data = get_r2_data()
    result = []
    for index, item in enumerate(data):
        d = string.digits # '0123456789'
        hot_content = item[0].rstrip(d) #去除最后的数字
        hot_value = item[0][len(hot_content):]
        keywords = extract_tags(hot_content) # jieba提取关键字
        for word in keywords:
            if not word.isdigit():
                flag = False
                for char in word: #判断关键字中是否有数字并剔除
                    if char.isdigit():
                        flag = True
                if flag:
                    continue
                result.append({
                    'name': word,
                    'value': 300 + (30 - int(index)) * 5 #构造权重
                })
    return jsonify({
        'keywords': result
    })

if __name__ == '__main__':
    app.run(port=PORT)