from app.main.modules.util.mysql.connector import connect_db
from time import sleep


def fetch(query: list, data: list = [], dictionary: bool = False, schema_name: str = 'report'):
    """
        Mysql Fetch 함수
        - 조회 작업에 사용
    """

    def callback(cursor):
        result = []
        for each_query in query:
            cursor.execute(each_query, data)
            response = cursor.fetchall()
            result.append({
                "columns": cursor.column_names,
                "rows": response,
            } if not dictionary else response)
        return result

    return connect_db(schema_name=schema_name, callback=callback, dictionary=dictionary)


def execute(statement: str, data: list, schema_name: str = 'report', log: bool = True):
    """
        Mysql Execute 함수
        - 조회 외의 작업에 사용
    """
    if data is None or len(data) == 0:
        data = [()]
    count = 0
    while True:
        try:
            connect_db(
                schema_name=schema_name,
                callback=lambda cursor: cursor.executemany(statement, data) if len(data) > 1 else cursor.execute(statement, data[0]),
                log=log
            )
            break
        except Exception as e:
            if "Lost Connection" in e:
                print(f'Error : {e}')
                count += 1
                sleep(5)
            else:
                raise e
        if count == 4:
            break
    return "Complete"


def call_procedure(procedure_name: str, data: list, dictionary: bool, schema_name: str = 'report'):
    """
            call mysql stored procedure
    """
    def callback(cursor):
        cursor.callproc(procedure_name, data)
        for result in cursor.stored_results():
            return result.fetchall()

    return connect_db(schema_name=schema_name, callback=callback, dictionary=dictionary)
