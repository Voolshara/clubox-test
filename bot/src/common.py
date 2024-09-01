from datetime import datetime, timedelta

def time_until_birthday(birthday: datetime.date):
    now = datetime.now()
    
    next_birthday = datetime(year=now.year, month=birthday.month, day=birthday.day)
    if next_birthday < now:
        next_birthday = datetime(year=now.year + 1, month=birthday.month, day=birthday.day)
    
    time_diff = next_birthday - now
    
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes = remainder // 60
    
    return days, hours, minutes
