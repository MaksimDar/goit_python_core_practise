# from datetime import datetime, timedelta

# "The patient need to know when to finish taking medicine, after 45 days"

# current_date = datetime.now()
# print(current_date)

# next_date = timedelta(current_date.day+45)

# print(current_date)

# final_date = current_date + next_date

# print(final_date.day)



from datetime import datetime, timedelta

"The patient need to know when to finish taking medicine, after 45 days"

current_date = datetime.now()
print(current_date)

next_date = timedelta(days=45)

day_on = current_date - next_date
day_off = current_date + next_date

print(day_on)
print(day_off)
print((day_off - day_on).days)




