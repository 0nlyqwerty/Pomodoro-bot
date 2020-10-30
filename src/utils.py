from datetime import datetime


def get_expire_time(minutes: int) -> datetime.datetime:
    """ get expire time after minutes from now
    args
        minutes: int
    return
        expire_time: datetime
    """
    now = datetime.datetime.now()
    expire_time = now + datetime.timedelta(minutes=minutes)
    return expire_time
