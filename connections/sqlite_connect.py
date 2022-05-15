import sqlite3 

def connect_db():
    conn=sqlite3.connect("mydb.db")
    conn.execute("create table if not exists testData (id int identity(1,1), name varchar(100), age int(3))")
    return conn

def execute_query(query,query_details=None):
    conn=connect_db()
    cursor=conn.cursor()
    data=[]
    if query_details is None:
        cursor.execute(query)
        data=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute(query,query_details)
        data=cursor.fetchall()
        conn.commit()
    return data
