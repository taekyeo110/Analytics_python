from app.main.config.env_config import OUTLOOK_USER, OUTLOOK_USER_SECOND
from app.main.modules.util.data.date import calculate_seconds, now
from app.main.modules.util.mysql.dml import insert
from app.main.modules.util.delivery.mail import send_mail


def logging(start_timestamp, end_timestamp, account_id, result, media, remote_type, start_seconds, end_seconds, is_success=False):
    """
            1. start_timestamp - store 함수에 포함
            2. end_timestamp - store 함수에 포함
            3. total_seconds
            4. account_id
            5. complete or error
            6. media
            7. store_or_merge
    """
    column_list = ["start_timestamp", "end_timestamp", "total_seconds", "account_id", "result", "media", "remote_type", "is_success"]
    if start_timestamp is None and end_timestamp is None:
        total_seconds = 0
        start_timestamp = now()
        end_timestamp = now()
    else:
        total_seconds = end_seconds - start_seconds
    if "error" in result or "Error" in result:
        send_mail(
            send_from=OUTLOOK_USER,
            send_to=[OUTLOOK_USER, OUTLOOK_USER_SECOND],
            subject=f'[자동발송] {remote_type} Error - {media}',
            text=f'{result}',
        )
    return insert(table_name="log_hermes.hermes_log", column=tuple(column_list),
                  data=[[str(start_timestamp), str(end_timestamp), float(total_seconds), account_id, result, media, remote_type, is_success],])
