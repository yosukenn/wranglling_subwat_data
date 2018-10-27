import pandas as pd
import pandasql

def num_rainy_days(filename):
    weather_data = pd.read_csv(filename)

    q = """
    SELECT sum(rain)
    FROM weather_data
    """

    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days
