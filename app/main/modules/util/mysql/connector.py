from mysql.connector import connect, Error
from app.main.config.db_config import MYSQL_CONFIG
from app.main.modules.util.logger.store import log_mysql_error
from typing import Callable


def connect_db(schema_name: str, callback: Callable, dictionary: bool = False, log: bool = True):
    """
        mysql 접속 및 실행 함수
    """
    connection = connect(database=schema_name, connection_timeout=1000, **MYSQL_CONFIG['hermes_server'])
    cursor = connection.cursor(buffered=True, dictionary=dictionary)
    try:
        result = callback(cursor)
        connection.commit()
        connection.close()
        return result if result is not None else cursor
    except Error as e:
        if log is True:
            # log_mysql_error(e.msg, e.errno, e.sqlstate)
            raise e
        connection.rollback()
        connection.close()
        raise e
