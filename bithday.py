from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    now = datetime.now()
    start, end = get_start_date(now)
    birthdays_storage = {}
    days = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=now.year)
        if start <= birthday <= end:
            weekday = birthday.weekday() if 0 <= birthday.weekday() <= 4 else 0
            birthdays_storage.setdefault(weekday, []).append(name)

    biggest_day_name = max(len(days[i]) for i in birthdays_storage.keys())
    for i in range(0, 5):
        birthdays = birthdays_storage.get(i)
        if birthdays:
            print(f'{days[i]:<{biggest_day_name}}: {", ".join(birthdays)}')

def get_start_date(current_date):
    current_date = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    day_diff = 6 - current_date.weekday()
    start = current_date + timedelta(days=day_diff - 1)
    end = start + timedelta(days=7, microseconds=-1)
    return start, end