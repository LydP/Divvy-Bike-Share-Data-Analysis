# Divvy Bike Share Data Anaylsis 

## Introduction 

This is my analysis of Divvy trip data for the Google Data Analytics certificate capstone project. My certificate can be seen [here](https://www.credly.com/badges/6e51f2de-b45a-4e2e-bff1-3da04eff93de). This repository contains the Python files I used to work with the data, a Google Colaboratory notebook that gives more detail on my thought process and conclusions alongside Python code, my analysis and conclusions in a PowerPoint, and my analysis and conclusions in a PDF report. 

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

These can be accessed directly [here](https://drive.google.com/file/d/1Nn8WDTX3wdeC5t9U3C87L7aoOVVNVtlT/view?usp=sharing). They are subject to [Divvy's Data License Agreement](https://www.divvybikes.com/data-license-agreement). 

## Files and Folders

### Divvy_Trip_Data_Analysis.ipynb

This is the Google Colaboratory notebook that describes my analysis and the data in more detail.

### Divvy_report.pdf

This is my analysis and conclusions presented in the form of a report. It's essentially a simplified version of the content in Divvy_Trip_Data_Analysis.ipynb.

### concat_csv.py

I used this code to combine the above files into a single CSV. This code also adds the columns ```ride_length``` and ```day_of_week``` to each CSV file and therefore to the final, concatenated file. Note that this file requires the folder raw_data containing the CSV files in order to work.

### plots.py

This file contains the class and corresponding methods that I used to generate the charts in the Plots folder. Note that this file requires the file divvy_trip_data_full.csv located in the raw_data directory (the result of running concat_csv.py) 

### Plots Folder

This folder contains JPG images of the plots produced by plots.py. It also contains the image Start Location Heat Map.png, which is a heat map made in Tableau Public of the start locations for each trip for August 2021. (The divvy_trip_data_full.csv file was too large for a Tableau Public upload). The workbook can be accessed [here](https://public.tableau.com/views/divvy_16346070460150/Sheet1?:language=en-US&:display_count=n&:origin=viz_share_link).

### Other Files

I also loaded the data from divvy_trip_data_full.csv in a DB file so that I could browse it with SQLite. That file is [here](https://drive.google.com/file/d/1Nn8WDTX3wdeC5t9U3C87L7aoOVVNVtlT/view?usp=sharing). 
