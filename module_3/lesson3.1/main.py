from datetime import datetime 
 ## also import is used from datetime import *  /////////////// is not recommended 

current_datetime = datetime.now() 

print(current_datetime)


date = datetime.today()

print(date)

print(current_datetime.date())
print(current_datetime.time())

print(current_datetime.year, current_datetime.month, current_datetime.day, current_datetime.hour)





