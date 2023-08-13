import datetime


def datetime_to_str(dt: datetime.datetime) -> str:
    return dt.isoformat()


def str_to_datetime(dt: str) -> datetime.datetime:
    return datetime.datetime.fromisoformat(dt)
