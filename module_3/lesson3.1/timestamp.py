# from datetime import datetime

# current_date = datetime.now()
# print(current_date.timestamp())

# day_zero = datetime.fromtimestamp(0)

# print(day_zero)

# print(current_date > day_zero)


# datetime_string = '1970:01:01 January Jan 03 03 00'

# readed_string = datetime.strptime(datetime_string, '%Y:%m:%d %B %b %H %M %S')

# print(readed_string)

# print(current_date.strftime('%Y-%m:%d %M'))


########################################

from datetime import datetime 

current_date = '2026-03-10'

requested_day = datetime.strptime(current_date, '%Y-%m-%d').date()
print(requested_day)

today_date = datetime.now().date()
diff_date = today_date - requested_day
print(diff_date.days)
