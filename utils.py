import pymysql


def get_database():
    db = pymysql.connect(host='localhost', user='root', passwd='123123123a', database='covid')
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
