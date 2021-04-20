'''
Tia Campagna
DS2500
Spring 2021
'''

'''
Gathers all the audio information for the top 200 tracks for each
month from March 2020 to April 2021
https://spotifycharts.com/regional
'''

import requests
import pandas as pd

CLIENT_ID = '319eae518516433ca75c177c1b0b9f6c'
CLIENT_SECRET = ''
AUTH_URL = 'https://accounts.spotify.com/api/token'
FILENAMES = ['Mar2020', 'Apr2020', 'May2020', 'Jun2020', 'Jul2020', 'Aug2020', 'Sep2020',
             'Oct2020', 'Nov2020', 'Dec2020', 'Jan2021', 'Feb2021', 'Mar2021', 'Apr2021']

def read_csv():
    '''
    Function: read_csv
    :return: together_df, a df containing the top songs for each month
    does: combines the csv files containing the top 200 songs for each month of the pandemic and labels them with
    a month number
    '''

    # initalizes an empty list of dataframes and the month number
    df_list = []
    month_num = 1

    # reads each csv file and labels the month number
    for file in FILENAMES:
        filename = file + '.csv'
        df = pd.read_csv(filename, header=0)
        df['Month Number'] = month_num
        month_num += 1
        # appends the list of dataframes
        df_list.append(df)

    # merges all the dataframes together
    together_df = pd.concat(df_list, axis=0, ignore_index=True)

    # keeps only columns containing the month number and track url and renames
    together_df.drop(together_df.columns.difference(['Unnamed: 4', 'Month Number']), 1, inplace=True)
    together_df.columns = ['Url', 'Month']
    together_df['ID'] = ''

    return together_df

def get_ids_df():
    '''
    function: get_ids_df
    :return: df, the dataframe appended with the track ID
    does: appends the dataframe with just the track ID of each top track for use in the Spotify API
    '''

    # reads the csv files into one large dataframe
    df = read_csv()

    # appends the ID column with the track ID
    for i in range(1, (len(df))):
        link = df.loc[i, 'Url']
        track_id = link.replace('https://open.spotify.com/track/', '')
        df.loc[i, 'ID'] = track_id

    return df

def find_tracks_info():
    '''
    Function: find_tracks_info
    :return: track_df, a dataframe containing all the audio features of the top 200 songs for each month
    during the pandemic
    does: makes requests to spotify api server, stores them in a dataframe and outputs them to a csv for use
    of other group members
    '''

    # creates a dataframe containing the track IDs of each top track
    df = get_ids_df()

    # POST a request w/ client credentials
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # Convert the response to JSON
    auth_response_data = auth_response.json()

    # Save the access token
    access_token = auth_response_data['access_token']

    # Send GET request to the API server w/ our access code
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    # Base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'

    # initializes an empty list
    tracks = []

    # integrates over the entire data frame
    for i in range(1, len(df)):
        # finds the track ID
        track_id = df.loc[i, 'ID']

        # actual GET request with proper header
        r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
        j = r.json()

        # appends the list of tracks with the specified audio features from the request
        if 'error' not in j:
            tracks.append([df.loc[i, 'Month'], df.loc[i, 'ID'], j['acousticness'], j['danceability'], j['duration_ms'],
                           j['energy'], j['instrumentalness'], j['liveness'], j['loudness'], j['mode'],
                           j['speechiness'], j['tempo'], j['time_signature'], j['valence']])

    # creates a dataframe containing the audio features for the top 200 tracks of each month
    track_df = pd.DataFrame(tracks, columns=['Month', 'ID', 'Acousticness', 'Danceability', 'Duration Ms', 'Energy',
                                       'Instrumentalness', 'Liveness', 'Loudness', 'Mode', 'Speechiness', 'Tempo',
                                       'Time Signature', 'Valence'])

    # writes the dataframe into a csv file so that other members can use the data without running the timely code
    track_df.to_csv(r'/Users/tiacampagna/Documents/DS2500/finalProject/topTracks.csv', header=True)

    return track_df

def find_monthly_averages():
    month_averages = pd.read_csv('topTracks.csv', parse_dates=['Month'], index_col='Month')
    month_averages = month_averages.groupby('Month').mean()
    for i in range(1, len(month_averages)+1):
        month_averages.loc[i, 'Date'] = FILENAMES[i-1]

    return month_averages

if __name__ == "__main__":

    # creates a dataframe containing the track info for the top 200 songs of each month of the pandemic
    # df = find_tracks_info()

    # let's you know when process has finished
    print('done')

