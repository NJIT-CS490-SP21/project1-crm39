import requests
import os
from dotenv import load_dotenv, find_dotenv
import random
from genius import get_lyrics

AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/artists/'

load_dotenv(find_dotenv())

def get_songs():
    
    songs = {}
    artist_ids = ('6TIYQ3jFPwQSRmorSezPxX', '6XyY86QOPPrYVGvF9ch6wz', '6C1ohJrd5VydigQtaGy5Wa')
    artist_id = artist_ids[random.randint(0,len(artist_ids)-1)]
    
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
    
    songs_data = requests.get(BASE_URL + artist_id + '/top-tracks?market=US', headers=headers)
    
    songs_json = songs_data.json()
    
    for song in songs_json['tracks']:
        song_name = song['name']
        song_artist = song['album']['artists'][0]['name']
        song_image = song['album']['images'][0]['url']
        song_preview = song['preview_url']
        song_lyrics = get_lyrics(song_name)
        
        
        song_info = (song_artist, song_image, song_preview, song_lyrics)
        
        # Dictionary containing each song as key and it's information in list format as the value
        songs[song_name] = song_info

    return songs
    
    # song name, artist, song-related image, preview URL
    
    # Linking Park: 6XyY86QOPPrYVGvF9ch6wz
    
    # MGK: 6TIYQ3jFPwQSRmorSezPxX
    
    # Joyner Lucas: 6C1ohJrd5VydigQtaGy5Wa