from connections.sqlite_connect import execute_query


def insert_data(data):
    try:
        query = '''insert into testData values(%s,%s)''', 
        (data['name'], data['age'])
        execute_query(query=query, query_details=data)
        return 'successfully inserted'
    except Exception as e:
        return e

def select_data():
    try:
        query = '''select * from testData'''
        result=execute_query(query=query)
        return result
    except Exception as e:
        return e
