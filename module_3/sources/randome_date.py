from datetime import datetime, timedelta
import random 

def get_random_birthdays(n):
    "Get a list of random birthdays"
    current_date = datetime.now()
    oldest_date = current_date - timedelta(days=365*80)
    
    birthdays_list = []
    


if __name__ == '__main__':
    get_random_birthdays(10)