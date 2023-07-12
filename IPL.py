import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv("Cricket_data.csv")


#
# data.shape
# print(data.columns)
def cleaning_the_data(data):
    data.drop(columns=['description', 'pom', 'highlights',
                       'home_key_batsman'
        , 'home_key_bowler', 'away_playx1', 'home_playx1', 'away_key_batsman', 'away_key_bowler', 'umpire1', 'umpire2',
                       'tv_umpire',
                       'referee', 'decision',
                       'reserve_umpire', 'match_days', 'points'], inplace=True)
    # print(data)

    data['winner'].fillna('No Player', inplace=True)
    data['1st_inning_score'].fillna(0, inplace=True)
    data['2nd_inning_score'].fillna(0, inplace=True)
    data['home_overs'].fillna(0, inplace=True)
    data['home_runs'].fillna(0, inplace=True)
    data['home_wickets'].fillna(0, inplace=True)
    data['home_boundaries'].fillna(0, inplace=True)
    data['away_overs'].fillna(0, inplace=True)
    data['away_runs'].fillna(0, inplace=True)
    data['away_wickets'].fillna(0, inplace=True)
    data['away_boundaries'].fillna(0, inplace=True)
    data['super_over'].fillna(0, inplace=True)

    # print(data.isna().sum().reset_index())

    data['start_date'] = pd.to_datetime(data['start_date'])
    data['super_over'] = data['super_over'].astype(bool)
    data['home_runs'] = data['home_runs'].astype('int16')
    data['home_wickets'] = data['home_wickets'].astype('int16')
    data['home_boundaries'] = data['home_boundaries'].astype('int16')
    data['away_runs'] = data['away_runs'].astype('int16')
    data['away_wickets'] = data['away_wickets'].astype('int16')
    data['away_boundaries'] = data['away_boundaries'].astype('int16')

    data['home_captain'].fillna('No Player', inplace=True)
    data['away_captain'].fillna('No Player', inplace=True)
    data['toss_won'].fillna('No data', inplace=True)
    data['season'].fillna('No data', inplace=True)

    data['city'] = ''
    for i in range(data.shape[0]):
        data.loc[i, 'city'] = data['venue_name'].str.split(', ')[i][-1]

    data = data[['season', 'id', 'name', 'short_name', 'home_team', 'away_team',
                 'toss_won', 'winner', 'start_date', 'venue_id',
                 'venue_name', 'city', 'home_captain', 'away_captain', 'super_over',
                 'home_overs', 'home_runs', 'home_wickets', 'home_boundaries',
                 'away_overs', 'away_runs', 'away_wickets', 'away_boundaries']]

    return data


def main():
    # print(data.info())
    cleaning_the_data(data)
    # print(data.isna().sum().reset_index())
    print(data.head())

    return data


main()
no_of_matches = data['season'].value_counts()
no_of_matches.plot(kind='bar', color='#ed7299')
plt.title('Number of Matches Played per Season')
plt.xlabel('Season')
plt.ylabel('Number of Matches Played')
plt.show()
