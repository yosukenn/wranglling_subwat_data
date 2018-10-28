import pandas as pd
import pandasql

def avg_weekend_temperature(filename):
    weather_data = pd.read_csv(filename)

    q = """
    SELECT
    avg(meantempi)
    FROM
    weather_data
    WHERE
    cast(strftime('%W', date) as integer) = 0 OR cast(strftime('%W', date) as integer) = 6
    """

    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends

print(avg_weekend_temperature('../datas/weather_underground.csv'))
