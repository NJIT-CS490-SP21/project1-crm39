import requests
import os
from dotenv import load_dotenv, find_dotenv

AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

load_dotenv(find_dotenv())

def get_songs():
    
    songs = []
    
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('SPOTIFY_KEY'),
        'client_secret': os.getenv('SPOTIFY_SECRET')
    })
    
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    
    headers = {
        'Authorization' : 'Bearer {token}'.format(token=access_token)
    }
    
    songs_data = requests.get(BASE_URL + 'browse/new-releases?country=US&offset=0&limit=10', headers=headers)
    
    songs_json = songs_data.json()
    
    
    for song in songs_json['albums']['items']:
        songs.append(song['name'])
        print(song['name'])

    return songs