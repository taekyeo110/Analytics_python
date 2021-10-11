import json
from app.main.modules.util.mysql.util import get_column_definition
from app.main.modules.util.mysql.tcl import execute


def check_data_type(data_list: list):
    """
            list 형식의 data
            ->
            data의 type을 하나하나 체크
            ->
            data의 type을 list로 return
    """
    data_type_list = []
    convert_data_list = []
    for data in data_list:
        if isinstance(data, int) and data is not True and data is not False:
            if len(str(data)) > 10:
                data_type_list.append('varchar(255)')
                convert_data_list.append(str(data))
            else:
                data_type_list.append('int(11)')
                convert_data_list.append(data)
        elif isinstance(data, str):
            data_type_list.append('varchar(255)')
            convert_data_list.append(data)
        elif isinstance(data, float):
            data_type_list.append('float')
            convert_data_list.append(data)
        elif isinstance(data, dict) or isinstance(data, list) or isinstance(data, tuple):
            data_type_list.append('json')
            convert_data_list.append(json.dumps(data))
        elif isinstance(data, bool):
            data_type_list.append('boolean')
            convert_data_list.append(data)
        elif data is True or data is False:
            data_type_list.append('boolean')
            convert_data_list.append(data)
        elif data is None:
            data_type_list.append('varchar(255)')
            convert_data_list.append('')
    return data_type_list, convert_data_list


def check_data_type_before_create_table(column_list: list, data_list: list):
    """
            data를 DB에 insert 하기 전에, table이 없다면 create를 해준다.
            그 때, data_list에 있는 data_type을 확인하여 create문에 넣을 수 있도록 한다.
            ->
            return column definition list
    """
    data_type_list = check_data_type(data_list)[0]
    return [get_column_definition(column_list[count], data_type_list[count]) for count in range(len(column_list))]


def convert_data_type_when_already_create_table(schema_name: str, table_name: str, column_list: list, data_list: list):
    """
            이미 DB에 테이블이 생성되어 있을 경우,
            테이블의 컬럼 정의를 바꿔준다.

            ALTER TABLE 테이블이름
            MODIFY COLUMN 컬럼명 변경할컬럼타입,
            ....,
            MODIFY COLUMN 컬럼명 변경할컬럼타입;
    """
    data_type_list = check_data_type(data_list)[0]
    modify_column_list = [f"MODIFY COLUMN `{column_list[count]}` {data_type_list[count]}" for count in range(len(column_list))]
    prepared_query = f"ALTER TABLE {schema_name}.{table_name} {', '.join(modify_column_list)};"
    print(prepared_query)
    return execute(prepared_query, [])
