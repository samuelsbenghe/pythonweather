import pandas as pd
import datetime


def format_time(timestamp: int):
    return pd.Timestamp(datetime.datetime.fromtimestamp(timestamp)).time()
