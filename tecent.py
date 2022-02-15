import pymysql
import time
import traceback
import requests
import json


def get_tencent_data():
    header = {'User-Agent':
                  r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'}
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    url2 = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList'
    res = requests.get(url, headers=header).json()
    res2 = requests.get(url2, headers=header).json()

    data = json.loads(res['data'])
    data2 = res2['data']

    history = {}

    for i in data2['chinaDayList']:
        ds = i['y'] + '.' + i['date']
        tup = time.strptime(ds, '%Y.%m.%d')
        ds = time.strftime('%Y-%m-%d', tup)
        history[ds] = {'confirm': i['confirm'],
                       'suspect': i['suspect'],
                       'heal': i['heal'], 'dead': i['dead']}

    for i in data2['chinaDayAddList']:
        ds = i['y'] + '.' + i['date']
        tup = time.strptime(ds, '%Y.%m.%d')
        ds = time.strftime('%Y-%m-%d', tup)
        history[ds].update({'confirm_add': i['confirm'],
                            'suspect_add': i['suspect'],
                            'heal_add': i['heal'], 'dead_add': i['dead']})

    details = []
    update_time = data['lastUpdateTime']
    data_province = data['areaTree'][0]['children']
    for pro_infos in data_province:
        province = pro_infos['name']
        for city_infos in pro_infos['children']:
            city = city_infos['name']
            confirm = city_infos['total']['confirm']
            confirm_add = city_infos['today']['confirm']
            heal = city_infos['total']['heal']
            dead = city_infos['total']['dead']
            details.append([update_time, province, city, confirm,
                            confirm_add, heal, dead])
    return {'history':history, 'details':details}


def insert_history(data:dict):
    try:
        print(f'{time.asctime()} 开始插入数据')
        cursor = db.cursor()
        for k, v in data.items():
            sql_query = f"insert into history values('{k}',{v['confirm']},{v['confirm_add']}," \
                        f"{v['suspect']},{v['suspect_add']},{v['heal']},{v['heal_add']}," \
                        f"{v['dead']},{v['dead_add']})"
            print(sql_query)
            cursor.execute(sql_query)
        db.commit()
        print(f'{time.asctime()} 完成插入数据')
    except:
        traceback.print_exc()
    finally:
        cursor.close()


def update_history(data:dict):
    try:
        print(f'{time.asctime()} 开始更新历史数据')
        cursor = db.cursor()
        sql = 'select confirm from history where ds=%s'
        for k, v in data.items():
            if not cursor.execute(sql, k):
                sql_query = f"insert into history values('{k}',{v['confirm']},{v['confirm_add']}," \
                            f"{v['suspect']},{v['suspect_add']},{v['heal']},{v['heal_add']}," \
                            f"{v['dead']},{v['dead_add']})"
                cursor.execute(sql_query)
        db.commit()
        print(f'{time.asctime()} 完成更新历史数据')
    except:
        traceback.print_exc()
    finally:
        if 'cursor' in locals().keys():
            cursor.close()


def update_details(data:list):
    cursor = None
    try:
        cursor = db.cursor()
        # 子查询，选中update_time字段，按照id字段的降序排列顺序，选出update_time字段第一个
        # 将返回的时间与我们传入的时间比较，相同返回1
        sql = 'select %s=(select update_time from details order by id desc limit 1)'
        # 指定插入顺序
        sql_query = f"insert into details (update_time,province,city,confirm,confirm_add," \
                    f"heal,dead) values(%s,%s,%s,%s,%s,%s,%s)"
        # print(data[0][0])
        cursor.execute(sql, data[0][0]) #对比最大时间戳
        result = cursor.fetchone()[0]
        if not result:
            print(f'{time.asctime()} 开始更新数据')
            for item in data:
                cursor.execute(sql_query, item)
            db.commit()
            print(f'{time.asctime()} 完成更新数据')
        else:
            print(f'{time.asctime()} 已是最新数据')
    except:
        traceback.print_exc()
    finally:
        if cursor:
            cursor.close()


if __name == '__main__':
    db = pymysql.connect(host='localhost', user='root', passwd='', database='covid')
    data = get_tecncent_data()
    print(data)
    # insert_history(data['history'])
    update_history(data['history'])
    update_details(data['details'])
    db.close()

