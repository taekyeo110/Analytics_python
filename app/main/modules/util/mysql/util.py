import json

from app.main.modules.util.data import camel_to_snake


def get_column_definition(column_name: str, data_type: str = "TEXT", default: str = "NULL", constraint: str = ""):
    """
            create table 시 column 정의
    """
    return f"{column_name} {data_type} {default} {constraint}"


def get_create_table_statement(table_name: str, column_definition_list: list):
    """
            create table
    """
    return f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
        {','.join(column_definition_list)}
        )
    """


def get_add_index_statement(table_name: str, index_name: str, column_list: list):
    """
            index 추가
    """
    return f"""
        ALTER TABLE {table_name} 
        ADD INDEX `{index_name}` ({','.join(column_list)})
    """


def get_add_column_statement(table_name: str, column_definition: str):
    """
            add column
    """
    return f"""
        ALTER TABLE {table_name} 
        ADD COLUMN {column_definition}
    """


def separate_dict_list(metric_list):
    """
            parameter
                metric_list: list(key: value 형식의 metric data들의 list)

            keys -> columns
            metrc의 keys -> row
    """
    if len(metric_list) == 0:
        return [], []

    columns = tuple(metric_list[0].keys())
    rows = []
    for metric in metric_list:
        tmp = []
        for column in columns:
            try:
                tmp.append(json.dumps(metric[column]) if (isinstance(metric[column], dict) or isinstance(metric[column], list)) else metric[column])
            except:
                tmp.append(None)
        rows.append(tuple(tmp))

    columns = tuple(map(lambda x: camel_to_snake(x), metric_list[0].keys()))
    return columns, rows
