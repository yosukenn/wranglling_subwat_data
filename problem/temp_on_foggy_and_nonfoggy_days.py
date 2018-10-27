import pandas as pd
import pandasql

def max_temp_aggregate_by_fog(filename):
    weather_data = pd.read_csv(filename)

    q = """
    SELECT fog, max(maxtempi)
    FROM weather_data
    GROUP BY fog
    """

    foggy_days = pandasql.sqldf(q.lower(), locals())
    return foggy_days

print(max_temp_aggregate_by_fog('../datas/weather_underground.csv'))
