'''
DS2500
Spring 2021
Accessing Spotfy API - Passing Access Token
Tia's Secret Info
'''

'''
Gets all the audio information from one singular track using the Spotify API
'''

import requests
import pandas as pd

CLIENT_ID = '319eae518516433ca75c177c1b0b9f6c'
CLIENT_SECRET = 'fa224dcd2e734d03b9b28664f4718bbd'
AUTH_URL = 'https://accounts.spotify.com/api/token'

if __name__ == "__main__":

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

"""EXAMPLE using Audio Features"""

# Base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# # Top Tracks ID from the URL
# playlist_id = ' '
#
# Track ID from the URI
track_id = '3BZEcbdtXQSo7OrvKRJ6mb'
#
# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
#
# Convert response to JSON
r = r.json()
print(r)
#
# #https://stmorse.github.io/journal/spotify-api.html


'''
Steps to getting this data:
1. download CSV file for each month
2. months = [Jan, Feb]
3. for month in months....read csv as a data frame
4. remove the track ID from the track URL and then append it to a different data frame
5. for track in data frame....
6. use spotfiy API to get the track attributes and then store it in the data frame
7. then you will have 12 data frames containing the track information of the top songs for 
the month
https://spotifycharts.com/regional/us/weekly/2021-02-26--2021-03-05
'''
