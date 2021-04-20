# -*- coding: utf-8 -*-
"""
Creating Genre CSV 
"""

import requests
import csv
import pandas as pd

BASE_URL = 'https://api.spotify.com/v1/'
CLIENT_ID = 'efd3bf7f5a234f33bb1bf73efb21266a'
CLIENT_SECRET = '584b7534ed544ff6bfaf3c870c0f7761'
AUTH_URL = 'https://accounts.spotify.com/api/token'

def ArtistDF (file):
    
    Artist = []
    ArtistCompilation = pd.DataFrame(columns=['Month','Artist', 'Artist ID', 'Song ID','Song Name', 
                                 'Song Popularity', 'Album Name', 'Album Release Date', 
                                 'Acousticness', 'Danceability', 'Duration Ms', 'Energy', 
                                 'Instrumentalness', 'Liveness', 'Loudness', 'Mode', 
                                 'Speechiness', 'Tempo', 'Time Signature', 'Valence'])

    for i in range(0, len(file)):
        
        track_id = file.loc[i, 'ID']
        r = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)
        j = r.json()
    
        if 'error' not in j:
            Artist.append([int(file.loc[i, 'Month']), j['artists'], file.loc[i, 'ID'], 
                           j['name'], j['popularity'], j['album']['name'], j['album']['release_date'], 
                           file.loc[i, 'Acousticness'], file.loc[i, 'Danceability'], file.loc[i, 'Duration Ms'], 
                           file.loc[i, 'Energy'], file.loc[i, 'Instrumentalness'], file.loc[i, 'Liveness'],
                           file.loc[i, 'Loudness'], file.loc[i, 'Mode'], file.loc[i, 'Speechiness'], 
                           file.loc[i, 'Tempo'], file.loc[i, 'Time Signature'], file.loc[i, 'Valence']])
            
    for row in Artist:
        for Artist_info in row[1]:
            ArtistCompilation.loc[len(ArtistCompilation)] = [row[0], Artist_info['name'], Artist_info['id'],
                                                             row[2], row[3], row[4], row[5], row[6], 
                                                             row[7], row[8], row[9], row[10], 
                                                             row[11], row[12], row[13], row[14],
                                                             row[15], row[16], row[17], row[18]]
    return ArtistCompilation


def GenreDF(file):
    
    Genre = []
    Genre_Artist = pd.DataFrame(columns=['Month','Artist', 'Artist ID', 'Song ID','Song Name', 
                                     'Song Popularity', 'Album Name', 'Album Release Date',
                                     'Genre 1', 'Genre 2', 'Genre 3', 'Genre 4',
                                     'Followers', 'Artist Popularity', 
                                     'Acousticness', 'Danceability', 'Duration Ms', 'Energy', 
                                     'Instrumentalness', 'Liveness', 'Loudness', 'Mode', 
                                     'Speechiness', 'Tempo', 'Time Signature', 'Valence'])
    for k in range(0, len(file)):
        
        # finds the track ID
        artist_id = file.loc[k, 'Artist ID']
    
        # actual GET request with proper header
        l = requests.get(BASE_URL + 'artists/' + artist_id, headers=headers)
        m = l.json()
    
        # appends the list of tracks with the specified genre/popularity from the request
        if 'error' not in m:
            Genre.append([int(file.loc[k, 'Month']), file.loc[k,'Artist'], 
                          file.loc[k, 'Artist ID'], file.loc[k, 'Song ID'],
                          file.loc[k, 'Song Name'], file.loc[k, 'Song Popularity'],
                          file.loc[k, 'Album Name'], file.loc[k, 'Album Release Date'],
                          m['genres'], m['followers'], m['popularity'], 
                          file.loc[k, 'Acousticness'], file.loc[k, 'Danceability'], int(file.loc[k, 'Duration Ms']), 
                          file.loc[k, 'Energy'], file.loc[k, 'Instrumentalness'], file.loc[k, 'Liveness'],
                          file.loc[k, 'Loudness'], int(file.loc[k, 'Mode']), file.loc[k, 'Speechiness'], 
                          file.loc[k, 'Tempo'], int(file.loc[k, 'Time Signature']), file.loc[k, 'Valence']])
    for row in Genre:   
        if len(row[8]) == 0 or len(row[8]) == 1 or len(row[8]) == 2 or len(row[8]) == 1 or len(row[8]) == 3: 
            row[8] += ['N/A'] * (4-len(row[8]))
        if len(row[8]) > 4:
            del row[8][4:]
        Genre_Artist.loc[len(Genre_Artist)] = [row[0], row[1], row[2], row[3], row[4], 
                                               row[5], row[6], row[7], 
                                               row[8][0], row[8][1], row[8][2], row[8][3], 
                                               row[9]['total'], row[10], 
                                               row[11], row[12], row[13], row[14], 
                                               row[15], row[16], row[17], row[18], 
                                               row[19], row[20], row[21], row[22]]    
    return Genre_Artist  


if __name__ == "__main__":

    auth_response = requests.post(AUTH_URL, {'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,'client_secret': CLIENT_SECRET,})
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

    Top200Songs = pd.read_csv('TopTrack2019.csv')
    Artist = ArtistDF(Top200Songs)  
    Genre_Artist = GenreDF(Artist)
        
    # writes the dataframe into a csv file so that other members can use the data without running the timely code
    Genre_Artist.to_csv(r'C:\Users\Joselyn\Documents\Spring_2021\DS2500_IntroToDataScience\Homework\TopGenres2019.csv', header=True)



