# Divvy Bike Share Data Anaylsis 

## Introduction 

This is my analysis of Divvy trip data for the Google Data Analytics certificate capstone project. My certificate can be seen [here](https://www.credly.com/badges/6e51f2de-b45a-4e2e-bff1-3da04eff93de). This repository contains the Python files I used to work with the data, a Google Colaboratory notebook that gives more detail on my thought process and conclusions alongside Python code, and my analysis and conclusions in a PowerPoint. 

## Data

Raw data and data other than what I used can be accessed [here](https://divvy-tripdata.s3.amazonaws.com/index.html). Of those files, I used the following:

```
202004-divvy-tripdata.zip
202005-divvy-tripdata.zip
202006-divvy-tripdata.zip
202007-divvy-tripdata.zip
202008-divvy-tripdata.zip
202009-divvy-tripdata.zip
202010-divvy-tripdata.zip
202011-divvy-tripdata.zip
202012-divvy-tripdata.zip
202101-divvy-tripdata.zip
202102-divvy-tripdata.zip
202103-divvy-tripdata.zip
202104-divvy-tripdata.zip
202105-divvy-tripdata.zip
202106-divvy-tripdata.zip
202107-divvy-tripdata.zip
202108-divvy-tripdata.zip
```

These can accessed directly [here](https://drive.google.com/file/d/1Nn8WDTX3wdeC5t9U3C87L7aoOVVNVtlT/view?usp=sharing). They are subject to [Divvy's Data License Agreement](https://www.divvybikes.com/data-license-agreement). 

## Files

### Divvy_Trip_Data_Analysis.ipynb

This is the Google Colaboratory notebook that describes my analysis in more detail.

### Divvy_presentation.pptx

This is the PowerPoint file containing the most pertinent points of my analysis and my conclusions and suggestions.

### concat_csv.py

I used this code to combine the above files into a single CSV. This code also adds the columns ```ride_length``` and ```day_of_week``` to each CSV file and therefore to the final, concatenated file. Note that this file requires the folder raw_data containing the CSV files in order to work.

### plots.py

This file contains the class and corresponding methods that I used to generate the charts in the Plots folder. Note that this file requires the file divvy_trip_data_full.csv located in the raw_data directory (the result of running concat_csv.py) 

### Other Files

I also loaded the data from divvy_trip_data_full.csv in a DB file so that I could browse it with SQLite. That file is [here](https://drive.google.com/file/d/1Nn8WDTX3wdeC5t9U3C87L7aoOVVNVtlT/view?usp=sharing). 
