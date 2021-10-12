"""concat_csv.py: concatenate the separate CSV files containing the Divvy trip data into a single CSV file and add
columns containing ride duration the day of the week on which the ride occurred"""

import glob
import pandas as pd

# raw_data contains the raw data from Divvy System Data
raw_csv = glob.glob(r'raw_data\*.csv')

csv_list = []
for csv in raw_csv:
    csv_input = pd.read_csv(csv, header=0, index_col=0)
    started_at = pd.to_datetime(csv_input['started_at'])
    ended_at = pd.to_datetime(csv_input['ended_at'])
    csv_input['ride_length'] = ended_at - started_at
    # Monday = 0, Sunday = 6
    csv_input['day_of_week'] = started_at.dt.dayofweek

    csv_input.to_csv(csv)
    csv_list.append(csv_input)

csv_df = pd.concat(csv_list)
csv_df.to_csv(r'raw_data\divvy-tripdata-full.csv')
print('DONE')
