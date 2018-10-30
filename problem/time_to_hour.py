import pandas

def time_to_hour(time):
    hstr = pandas.to_datetime(time)
    hour = hstr.hour

    return hour

print(time_to_hour('12:22:22'))
