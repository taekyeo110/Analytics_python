from mysql.connector import Error

from app.main.modules.util.data.text import camel_to_snake
from app.main.modules.util.mysql.util \
    import get_add_index_statement, get_add_column_statement, get_create_table_statement, get_column_definition
from app.main.modules.util.mysql.tcl import execute, fetch


def create_table(table_name: str, column_definition_list: list, schema_name: str = 'report'):
    """
        Mysql 테이블 생성 함수
    """
    statement = get_create_table_statement(table_name, column_definition_list)
    print(statement)
    return execute(statement=statement, data=[], schema_name=schema_name)


def create_data_table(table_name: str, columns: list, schema_name: str = 'report'):
    if not describe_table(schema_name=schema_name, table_name=table_name):
        create_table(
            table_name=camel_to_snake(table_name),
            column_definition_list=
            [get_column_definition('raw_id', 'int', 'AUTO_INCREMENT', 'PRIMARY KEY')] +
            list(map(lambda x: get_column_definition(camel_to_snake(x)), columns)) +
            [get_column_definition('_created', 'datetime', 'DEFAULT CURRENT_TIMESTAMP')],
            schema_name=schema_name
        )
        print(f"Table created: {schema_name}.{table_name}")


def add_column(table_name: str, column_definition: str, schema_name: str = 'report'):
    """
        Mysql 칼럼 생성 함수
    """
    statement = get_add_column_statement(table_name, column_definition)
    return execute(statement=statement, data=[], schema_name=schema_name)


def add_index(table_name: str, index_name: str, column_list: list, schema_name: str = 'report'):
    """
        Mysql 칼럼 생성 함수
    """
    statement = get_add_index_statement(table_name, index_name, column_list)
    return execute(statement=statement, data=[], schema_name=schema_name)


def describe_table(schema_name: str, table_name: str):
    """
            주석
    """
    try:
        statement = f"DESCRIBE `{schema_name}`.`{table_name}`"
        return fetch([statement])[0]
    except Error as e:
        return False
