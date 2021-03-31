# -*- coding: utf-8 -*-
"""
Accessing Spotfy API - Passing Access Token
"""

import requests

CLIENT_ID = 'efd3bf7f5a234f33bb1bf73efb21266a'
CLIENT_SECRET = '584b7534ed544ff6bfaf3c870c0f7761'
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

# Track ID from the URI
track_id = '6y0igZArWVi6Iz0rj35c1Y'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

# Convert response to JSON
r = r.json()
print(r)

#https://stmorse.github.io/journal/spotify-api.html