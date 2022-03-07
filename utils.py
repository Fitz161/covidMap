import pymysql

from config import *

def get_database():
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWORD, database=DATABASE)
    if db.open:
        cursor = db.cursor()
        return db, cursor
    else:
        raise Exception('数据库连接失败')

def close_database(db, cursor):
    cursor.close()
    db.close()

def query(sql:str, *args):
    db, cursor = get_database()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    close_database(db, cursor)
    return result

def get_c1_data()->tuple:
    sql = """
    select 
    (select max(confirm) from history),
    (select confirm_add from history order by ds desc limit 1),
    sum(heal),
    sum(dead)
    from details
    where update_time=(select update_time from details order by update_time desc limit 1)
    """
    #select语句可以嵌套
    #select update_time from details order by update_time desc limit 1
    #按时间字段倒叙排序，选中第一个（即时间最新的），然后执行前面的sum操作
    return query(sql)[0]

def get_c2_data():
    sql = """
    select province,sum(confirm_add) from details
    where update_time=(select update_time from details order by update_time desc limit 1)
    group by province
    """
    # group by province将province字段相同的条目分成一组，
    # select province,sum(confirm) 选出每一组中的province字段，和每一组中confirm字段sum后的数据
    return query(sql)

def get_l1_data():
    sql = """
    select ds,confirm,suspect,heal,dead from history
    """
    return query(sql)

def get_l2_data():
    sql = """
    select ds,confirm_add,suspect_add from history
    """
    return query(sql)

def get_r1_data():
    sql = """
    select city,confirm from
    (
    select city,confirm from details
    where update_time=(select update_time from details order by update_time desc limit 1)
    and province not in ("北京","上海","天津","重庆")
    union all
    select province as city,sum(confirm) as confirm from details
    where update_time=(select update_time from details order by update_time desc limit 1)
    and province in ("北京","上海","天津","重庆") group by province 
    )
    as city_confirm
    order by confirm desc limit 5
    """
    # 中间部分的上半部分选中了province为非直辖市的最新记录，下半部分选中province为直辖市的最新记录，
    # 然后按照province分组，并将每组中province字段作为city字段的内容，sum(confirm)更名为confirm
    # 即将一个直辖市下几个区的确诊数据合并到一起，union 拼接组合两个结果表，all表示不消除重复行
    # 生成的表必须要有名称，as city_confirm指定表名为city_confirm
    sql2 = """
    select province,sum(confirm_add) as confirm_add from details
    where update_time=(select update_time from details order by update_time desc limit 1)
    group by province
    order by confirm_add desc limit 5
    """
    # 获取新增确诊最多的省份/地区
    return query(sql2)

def get_r2_data():
    sql = 'select content from ' \
          '(select id,content from hotsearch order by id desc limit 30) as a ' \
          'order by id asc'
    #先取最后三十个（最新数据），再逆序输出（使热度高的在前）
    return query(sql)
