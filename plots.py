"""plots.py: create plots to visualize Divvy trip data."""

import matplotlib.pyplot as plt
import pandas as pd


class DivvyPlots:
    """
    This class contains methods for creating different plots specifically for visualizing Divvy trip data
    """
    def __init__(self):
        """
        Init DivvyPlots
        """
        self.df = pd.read_csv(r"raw_data\divvy-tripdata-full.csv", header=0)
        self.member_df = self.df.loc[self.df.member_casual == 'member']
        self.casual_df = self.df.loc[self.df.member_casual == 'casual']

    def end_time_of_ride_per_day(self):
        """
        Create and save a bar chart showing the hour when Divvy users end their rides for each day of the week
        :return: None
        """

        member_df = self.member_df.reset_index()
        casual_df = self.casual_df.reset_index()

        member_df['ended_at'] = pd.to_datetime(member_df['ended_at']).dt.hour
        casual_df['ended_at'] = pd.to_datetime(casual_df['ended_at']).dt.hour

        member_df_time = member_df.groupby('day_of_week')['ended_at'].value_counts()
        casual_df_time = casual_df.groupby('day_of_week')['ended_at'].value_counts()

        max_list = []
        for i in range(7):
            max_list.append([member_df_time[i].idxmax(), casual_df_time[i].idxmax()])

        temp_df = pd.DataFrame(max_list, columns=['full members', 'casual members'])
        temp_df.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        ax = temp_df.plot.bar(rot=0)
        ax.legend(['full members', 'casual members'])
        ax.set_title('Most Common End Time for Each Day')
        plt.ylabel('ended_at (hour of day)')
        ax.set_ylim(0, 23)
        plt.yticks(range(23))

        plt.savefig(r'end_time_day_bar.jpg')

    def start_time_of_ride_per_day(self):
        """
        Create and save a bar chart showing the hour when Divvy users start their rides for each day of the week
        :return: None
        """

        member_df = self.member_df.reset_index()
        casual_df = self.member_df.reset_index()

        member_df['started_at'] = pd.to_datetime(member_df['started_at']).dt.hour
        casual_df['started_at'] = pd.to_datetime(casual_df['started_at']).dt.hour

        member_df_time = member_df.groupby('day_of_week')['started_at'].value_counts()
        casual_df_time = casual_df.groupby('day_of_week')['started_at'].value_counts()

        max_list = []
        for i in range(7):
            max_list.append([member_df_time[i].idxmax(), casual_df_time[i].idxmax()])

        temp_df = pd.DataFrame(max_list, columns=['full members', 'casual members'])
        temp_df.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        ax = temp_df.plot.bar(rot=0)
        ax.legend(['full members', 'casual members'])
        ax.set_title('Most Common Start Time for Each Day')
        plt.ylabel('started_at (hour of day)')
        ax.set_ylim(0, 23)
        plt.yticks(range(23))

        plt.savefig(r'start_time_day_bar.jpg')

    def time_of_ride(self):
        """
        Create a bar chart showing the distribution of hours of the day when Divvy users begin their rides for a single
        day
        :return: None
        """

        member_df = self.member_df.reset_index()
        casual_df = self.casual_df.reset_index()

        member_df['started_at'] = pd.to_datetime(member_df['started_at']).dt.hour
        casual_df['started_at'] = pd.to_datetime(casual_df['started_at']).dt.hour

        member_df_size = member_df.groupby('started_at')['member_casual'].size()
        casual_df_size = casual_df.groupby('started_at')['member_casual'].size()

        temp_df = pd.concat([member_df_size, casual_df_size], axis=1)

        ax = temp_df.plot.bar(rot=0)
        ax.legend(['full members', 'casual members'])
        ax.set_title('Time of Day Members Are Riding')
        plt.xlabel('started_at (hour of day)')

        plt.savefig(r'time_bar.jpg')

    def station_usage(self):
        """
        Create a bar chart showing the 15 stations most frequented by casual members
        :return: None
        """

        casual_df_size_start = self.casual_df.groupby('start_station_name')['member_casual'].size().nlargest(15)
        casual_df_size_start = pd.DataFrame(casual_df_size_start)

        ax = casual_df_size_start.plot.barh()
        ax.set_title('15 Stations Most Popular With Casual Members')
        plt.tight_layout()

        plt.savefig(r'casual_start_station_usage.jpg')

    def member_day_length_bar(self):
        """
        Create a bar chart showing how long most Divvy members spend on their bike trips for each day of the week
        :return: None
        """

        member_df = self.member_df.reset_index()
        casual_df = self.casual_df.reset_index()

        # round ride_length strings to minutes
        member_df['ride_length'] = pd.to_timedelta(member_df['ride_length']).astype('timedelta64[m]')
        casual_df['ride_length'] = pd.to_timedelta(casual_df['ride_length']).astype('timedelta64[m]')

        # remove outliers (>3 STDs from mean and less than 0)
        member_index = member_df['ride_length'].index[
            (member_df['ride_length'] > (member_df['ride_length'].mean() + 3 * member_df['ride_length'].std())) | (member_df['ride_length'] < 0)]
        casual_index = casual_df['ride_length'].index[
            (casual_df['ride_length'] > (casual_df['ride_length'].mean() + 3 * casual_df['ride_length'].std())) | (casual_df['ride_length'] < 0)]

        member_df.drop(labels=member_index, inplace=True)
        casual_df.drop(labels=casual_index, inplace=True)

        member_ride_length = member_df.groupby('day_of_week')['ride_length'].mean()
        casual_ride_length = casual_df.groupby('day_of_week')['ride_length'].mean()

        temp_df = pd.concat([member_ride_length, casual_ride_length], axis=1)

        temp_df.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        ax = temp_df.plot.bar(rot=0, ylabel='Ride Time (minutes)', legend=True)
        ax.legend(['full members', 'casual members'])
        ax.set_title('How Long Members Are Riding Per Day')

        plt.savefig(r'day_ride_length_bar.jpg')

    def member_day_bar(self):
        """
        Create a bar chart showing the distribution of which day of the week members use Divvy
        :return: None
        """

        member_day_size = self.member_df.groupby('day_of_week')['member_casual'].size()
        casual_day_size = self.casual_df.groupby('day_of_week')['member_casual'].size()

        temp_df = pd.concat([member_day_size, casual_day_size], axis=1)

        temp_df.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        ax = temp_df.plot.bar(rot=0)
        ax.legend(['full members', 'casual members'])
        ax.set_title('Days of the Week Members Are Riding')

        plt.savefig(r'day_bar.jpg')

    def member_time_hist(self):
        """
        Create a histogram chart showing the distribution of rider's ride times
        :return: None
        """

        member_ride_length = self.member_df.reset_index()['ride_length']
        casual_ride_length = self.casual_df.reset_index()['ride_length']

        # round ride_length strings to minutes
        member_ride_length = pd.to_timedelta(member_ride_length).astype('timedelta64[m]')
        casual_ride_length = pd.to_timedelta(casual_ride_length).astype('timedelta64[m]')

        # remove outliers (>3 STDs from mean and less than 0)
        member_index = member_ride_length.index[
            (member_ride_length > (member_ride_length.mean() + 3 * member_ride_length.std())) | (member_ride_length < 0)]
        casual_index = casual_ride_length.index[
            (casual_ride_length > (casual_ride_length.mean() + 3 * casual_ride_length.std())) | (casual_ride_length < 0)]

        member_ride_length.drop(labels=member_index, inplace=True)
        casual_ride_length.drop(labels=casual_index, inplace=True)

        temp_df = pd.concat([member_ride_length, casual_ride_length], axis=1)
        temp_df.set_axis(['full members', 'casual members'], axis='columns', inplace=True)

        temp_df.plot.hist(alpha=0.25, ec='black', logy=True)
        plt.xlabel('Ride Time (minutes)')
        plt.ylabel('log(Frequency)')
        plt.title('Distribution of Casual and Full Member Ride Times')

        plt.savefig(r'member_time_hist.jpg')

    def member_bike_bar(self):
        """
        Create a bar chart showing how many Divvy members use each category of rideable_type
        :return: None
        """

        member_df_size = self.member_df.groupby('rideable_type')['member_casual'].size()
        casual_df_size = self.casual_df.groupby('rideable_type')['member_casual'].size()

        temp_df = pd.concat([member_df_size, casual_df_size], axis=1)

        ax = temp_df.plot.bar(rot=0)
        ax.legend(['full members', 'casual members'])
        ax.set_title('Casual and Full Member Bike Usage')

        plt.savefig(r'bike_bar.jpg')
