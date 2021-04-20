# -*- coding: utf-8 -*-
"""
Accessing Spotfy API - Passing Access Token
"""

import requests
import csv
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


CLIENT_ID = 'efd3bf7f5a234f33bb1bf73efb21266a'
CLIENT_SECRET = '584b7534ed544ff6bfaf3c870c0f7761'
AUTH_URL = 'https://accounts.spotify.com/api/token'

if __name__ == "__main__":

    # POST a request w/ client credentials 
    auth_response = requests.post(AUTH_URL, 
    {
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

Top200Songs = pd.read_csv('TopTracks.csv')
Top200Songs = Top200Songs.head(15)
Artist = []
Genre = []
Month_Artist = pd.DataFrame(columns=['Month','Artist', 'Artist ID', 'Song Name', 
                                     'Song Popularity'])
Genre_Artist = pd.DataFrame(columns=['Month','Artist', 'Artist ID', 'Song Name', 
                                     'Song Popularity', 'Genre 1', 'Genre 2', 
                                     'Genre 3','Followers', 'Artist Popularity'])

for i in range(0, len(Top200Songs)):
    
    # finds the track ID
    track_id = Top200Songs.loc[i, 'ID']

    # actual GET request with proper header
    r = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)
    j = r.json()

    # appends the list of tracks with the specified audio features from the request
    if 'error' not in j:
        Artist.append([int(Top200Songs.loc[i, 'Month']), j['artists'], 
                       j['name'], j['popularity']])

for row in Artist:
    for Artist_info in row[1]:
        Month_Artist.loc[len(Month_Artist)] = [row[0], Artist_info['name'], Artist_info['id'],
                                               row[2], row[3]]

for k in range(0, len(Month_Artist)):
    
    # finds the track ID
    artist_id = Month_Artist.loc[k, 'Artist ID']

    # actual GET request with proper header
    l = requests.get(BASE_URL + 'artists/' + artist_id, headers=headers)
    m = l.json()

    # appends the list of tracks with the specified genre/popularity from the request
    if 'error' not in m:
        Genre.append([int(Month_Artist.loc[k, 'Month']), Month_Artist.loc[k,'Artist'], 
                      Month_Artist.loc[k, 'Artist ID'],Month_Artist.loc[k, 'Song Name'], 
                      Month_Artist.loc[k, 'Song Popularity'], m['genres'], m['followers'],
                      m['popularity']])
for row in Genre:   
    if len(row[5]) == 2:
        Genre_Artist['Genre 3'] = 'N/A'
        continue
        Genre_Artist.loc[len(Genre_Artist)] = [row[0], row[1], row[2], row[3], row[4], 
                                               row[5][0], row[5][1], row[5][2], 
                                               row[6]['total'], row[7]]

# writes the dataframe into a csv file so that other members can use the data without running the timely code
Genre_Artist.to_csv(r'C:\Users\Joselyn\Documents\Spring_2021\DS2500_IntroToDataScience\Homework\TopGenres2020.csv', header=True)

# ALL_ArtistperMo = Month.groupby(['Month']).Artist.value_counts().sort_values(ascending=False)
# ArtistperMo = ALL_ArtistperMo.rename('Count')

# ArtistperMo = ALL_ArtistperMo.groupby('Month').head(3)
# ArtistperMo = ArtistperMo.reset_index()

# fig = plt.figure(figsize=(19.20,10.80))
# fg = sns.catplot(x='Month', y='Count', hue= 'Artist', kind="bar", data=ArtistperMo)


