from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')

def calculate_future_date():
    num_of_days = int(input('Input the number os days: '))
    future_date = datetime.now() + timedelta(days=num_of_days)

    print(f'Future date: {future_date.strftime("%Y-%m-%d")}')

display_current_datetime()
calculate_future_date()