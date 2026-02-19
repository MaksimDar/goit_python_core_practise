from datetime import datetime, timedelta

def get_days():
    """ Script of calculating days until input date"""
    user_input = input("Input date in the format dd.mm: ")
    user_date = datetime.strptime(user_input, '%d.%m')
    current_date = datetime.now()
    user_date = user_date.replace(year = current_date.year)
    delta_days = user_date - current_date

    target_date = datetime.strftime(user_date, '%d-%B-%Y')
    if delta_days.days > 0:
        print(f"{delta_days.days} days left before {target_date}")
    else:
        print("Add one year")
        user_date = user_date.replace(year=user_date.year+1)
        delta_days = user_date - current_date
        print(f"{delta_days.days} days left {target_date}")

def make_backup(data):
    current_time = datetime.now()
    with open(f"backup_{current_time.timestamp()}.txt", "w") as fh:
        fh.write(data)


if __name__ == '__main__':
    get_days()
    data="Hello"
    make_backup(data)