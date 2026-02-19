############ Find out datatime
# import datetime 

# now = datetime.datetime.now()

# print(now)


# from datetime import datetime 

# current_time = datetime.now()

# print(f"Current time: {current_time}")

# print(f"Current year: {current_time.year}")
# print(f"Current Month: {current_time.month}")
# print(f"Current day: {current_time.day}")
# print(f"Current hour: {current_time.hour}")
# print(f"Current minute: {current_time.minute}")
# print(f"Current second: {current_time.second}")
# print(f"Current microsecond: {current_time.microsecond}")
# print(f"Current tzinfo: {current_time.tzinfo}")

# print(f"Date: {current_time.date()}")
# print(f"Today's time: {current_time.time()}")


############## Create combined data object

# import datetime

# current_date = datetime.date(2026,2,18)
# current_time = datetime.time(12, 36, 34)

# combined_datetime = datetime.datetime.combine(current_date, current_time)

# print(f"Combined datatime: {combined_datetime}")

#################### Create a Data Object

# import datetime

# created_time = datetime.datetime(year=2006,month=3,day=19)
# created_fulltime = datetime.datetime(year=2006,month=3,day=19, hour=22,minute=16,second=14)

# print(f"Created Time: {created_time}")
# print(f"Created FullTime: {created_fulltime}")

############## Find a weekday

# from datetime import datetime

# currently_time = datetime.now()

# weekday = currently_time.weekday()

# print(f"Weekday: {weekday}")

############### Comparing two objects

# from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)

# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

###########Timedelta

# from datetime import timedelta

# primary_time = timedelta(
#     days=8,
#     seconds=24,
#     minutes=45,
#     weeks=4
# )

# print(primary_time)


############## Отримання порядкового номера

# from datetime import datetime

# # Створення об'єкта datetime
# date = datetime(year=2023, month=12, day=18)

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")


#################################
# from datetime import datetime
# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)
# # Поточна дата
# current_date = datetime.now()
# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)


###############################
# from datetime import datetime

# now = datetime.now()

# Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)


##########################. ISO 8601

# from datetime import datetime

# # Поточна дата та час
# now = datetime.now()

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)

########## astimezone
# from datetime import datetime, timezone, timedelta

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=+2)))
# # Перетворює час UTC в час Східного часового поясу
# print(eastern_time)  



# # Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)  # Виведе час в UTC


############## sleep() method
# import time

# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")


############ localtime()
# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# local_time = time.localtime(current_time)
# print(f"Місцевий час: {local_time}")

########## perf_counter method

# import time

# # Записуємо час на початку виконання
# start_time = time.perf_counter()

# # Виконуємо якусь операцію
# for _ in range(1_000_000):
#     pass  # Просто проходить цикл мільйон разів

# # Записуємо час після виконання операції
# end_time = time.perf_counter()

# # Розраховуємо та виводимо час виконання
# execution_time = end_time - start_time
# print(f"Час виконання: {execution_time} секунд")















