import pandas as pd
import pandasql

def avg_min_temperature(filename):
    weather_data = pd.read_csv(filename)

    q = """
    SELECT
    avg(cast(mintempi as integer))
    FROM
    weather_data
    WHERE
    rain = 1 AND cast(mintempi as integer) > 55
    """

    avg_min_temp_rainy = pandasql.sqldf(q.lower(), locals())
    return avg_min_temp_rainy

print(avg_min_temperature('../datas/weather_underground.csv'))
