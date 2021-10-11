from app.main.config.db_config import ES_HOST
from elasticsearch import Elasticsearch

es = Elasticsearch([ES_HOST])


def index(target_index: str, body: dict, target_id=None):
    """
            elasticsearch index
                -> MySQL Insert
                -> 리소스 관리 문제로 미사용
    """
    print(index)
    return es.index(index=target_index, id=target_id, body=body)

def get(target_index: str, target_id: int):
    """
            elasticsearch get
                -> MySQL Select
                -> 리소스 관리 문제로 미사용
    """
    print(index)
    return es.get(index=target_index, id=target_id)

def search(target_index: str, body: dict):
    """
            elasticsearch search
                -> MySQL Select
                -> 리소스 관리 문제로 미사용
    """
    print(index)
    return es.search(index=target_index, body=body)

def refresh(target_index: str):
    """
            elasticsearch refresh
                -> MySQL Update
                -> 리소스 관리 문제로 미사용
    """
    print(index)
    return es.indices.refresh(index=target_index)
