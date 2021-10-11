from app.main.modules.util.mysql.tcl import execute, fetch


def select(query: str or list, data=(), dictionary: bool = False, schema_name: str = 'report'):
    """
            MySQL Select 함수
    """
    if isinstance(query, list):
        return fetch(query, data, dictionary, schema_name)
    else:
        return fetch([query], data, dictionary, schema_name)[0]


def insert(table_name: str, column: tuple, data: list, schema_name: str = 'report'):
    """
        Mysql Insert 함수
    """
    if len(data) == 0:
        return
    statement = f"""INSERT INTO {table_name} {str(column).replace("'", "`")} VALUES {str(tuple(map(lambda x: '%s', column))).replace("'", "")}"""
    print(f"INSERT INTO {schema_name}.{table_name} / Length:{len(data)}")
    count = 0
    while count < len(data):
        execute(
            statement=statement,
            data=data[count:count+10000],
            schema_name=schema_name
        )
        count += 10000


def update(table_name: str, key_column: str, target_columns: tuple, data: list, schema_name: str = 'report'):
    """
        Mysql Update 함수
        *Data 파라미터 형식
            data = [
                {
                    "key": Key Column Value,
                    "value": ('Value1', 'Value2', 'Value3', 'Value4'...)
                },...
            ]
    """
    statement = f"""
        UPDATE {table_name} 
        SET {', '.join(list(map(lambda x: f"{x} = %s", target_columns)))} 
        WHERE {key_column} = %s 
    """

    return execute(
        statement=statement,
        data=list(map(lambda x: (x["value"] + (x["key"],)), data)),
        schema_name=schema_name
    )


def delete(table_name: str, key_column: str, key_list: list, schema_name: str = 'report'):
    """
        Mysql Delete 함수
    """
    statement = f"""
        DELETE FROM {table_name} 
        WHERE {key_column} = %s
    """

    return execute(
        statement=statement,
        data=list(map(lambda x: (x,), key_list)),
        schema_name=schema_name
    )
