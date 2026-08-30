from datetime import datetime


def format_long_date(time: int):
    template = "%y-%b-%d %H:%M:%S"
    return datetime.fromtimestamp(time).strftime(template)
