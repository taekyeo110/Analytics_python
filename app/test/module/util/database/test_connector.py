from app.main.modules.util.mysql.connector import connect_db


def test_connect_db():
    def callback(cursor):
        cursor.execute('SELECT NOW()', [])
        return cursor.fetchall()

    result = connect_db('hermes_server', callback)
    print(f"\nTEST Result: {result}")
    assert isinstance(result, list)

