import datetime

def reformat_subway_dates(data):
    # month-day-year -> year-month-day

    date_formatted = datetime.datetime.strptime(date, '%m-%d-%y').date()
    return date_formatted
