from datetime import datetime, timedelta

def calculate_days_ago(start_date, end_date):
    start_datetime = datetime.strptime(start_date, "%d/%m/%Y")
    end_datetime = datetime.strptime(end_date, "%d/%m/%Y")
    delta = end_datetime - start_datetime
    return delta.days
