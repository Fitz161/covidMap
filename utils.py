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

