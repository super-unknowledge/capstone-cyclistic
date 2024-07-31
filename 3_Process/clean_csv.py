import pandas as pd
import numpy as np

# open csv
df = pd.read_csv(filename)

# count blank values per column
df.isnull().sum()

# check unique values per column
df.column_name.unique()

# check count of unique values per column
df.nunique(axis=0)

# check column datatypes
df.dtypes

# get df summary
df.info()

# change start and end columns to datetime
df["started_at"] = pd.to_datetime(df["started_at"], format='%Y-%m-%d %H:%M:%S')

# check for duplicates by ID
df[df.duplicated(['ride_id'], keep=False)]

# remove rows where essential column is empty
df['end_station_id'].replace('', np.nan, inplace=True)
df.dropna(subset=['end_station_id'], inplace=True)

# compute ride duration
df['ride_length'] = df.apply(lambda row: row.ended_at - row.started_at, axis=1)

# create column for day of the week each ride started
df['day_of_week'] = df.apply(lambda row: row.started_at.dayofweek, axis=1)

