from app.main.modules.util.data import now, date
from app.main.modules.util.es import elasticsearch


def log_job(title: str, hour, minute, second):
    """
        스케쥴 작업 실행 로그 적재
    """
    doc = {
        "title": title,
        "hour": hour,
        "minute": minute,
        "second": second,
        "timestamp": now(),
    }
    print(f"log_job: title: {title} hour: {hour} minute: {minute} second: {second}")
    return elasticsearch.index("logger-job", doc)


def log_request(method: str, url: str, status_code: int, total_seconds, headers: dict):
    """
        Request 로그 적재
    """
    doc = {
        "status_code": status_code,
        "method": method,
        "url": url,
        "total_seconds": total_seconds,
        "headers": headers,
        "timestamp": now(),
    }
    print(f"log_request: status_code: {status_code} method: {method} url: {url[:50]} total_seconds: {total_seconds}")
    return elasticsearch.index("logger-request", doc)


def log_mysql_error(msg: str, errno: int, sqlstate: str):
    """
        Mysql error_log 수집 쿼리 실행 함수
    """
    doc = {
        "msg": msg,
        "errno": errno,
        "sqlstate": sqlstate,
        "timestamp": now(),
    }
    print(f"log_mysql_error: msg: {msg} errno: {errno} sqlstate: {sqlstate}")
    return elasticsearch.index("logger-mysql-error", doc)


def log_send_mail(send_from: str, send_to: list, subject: str, text: str = None, html: str = None, files=None):
    """
        Mysql error_log 수집 쿼리 실행 함수
    """
    doc = {
        "send_from": send_from,
        "send_to": send_to,
        "subject": subject,
        "text": text,
        "html": html,
        "files": files,
        "timestamp": now(),
    }
    print(f"log_mysql_error: msg: {send_from} errno: {send_to} sqlstate: {subject}")
    return elasticsearch.index("logger-send-mail", doc)
