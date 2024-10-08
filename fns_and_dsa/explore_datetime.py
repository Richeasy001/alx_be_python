from datetime import datetime, timedelta


def display_current_datetime():
    current_datetime = datetime.now()
    current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date and time: {current_datetime}"


number_of_days = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    future_date = datetime.now() + timedelta(days=number_of_days)
    future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    return f"Future date: {future_date}"
