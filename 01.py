from datetime import datetime

def get_days_from_today(date):
    target_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.now()
    delta = (target_date - today).days
    return delta
date_input = "2020-10-09"
days_difference = get_days_from_today(date_input)
print(f"Numbers of days from {date_input}: {days_difference}")

