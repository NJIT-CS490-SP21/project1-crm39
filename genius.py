import requests
import os
from dotenv import load_dotenv, find_dotenv

BASE_URL = 'https://api.genius.com/search'
BASE_LINK_URL = 'https://genius.com'

load_dotenv(find_dotenv())

def get_lyrics(song_name):
    
    song_name.replace(' ', '%20') # %20 is the space character for the get request
    # try using params. It'll avoid the need for the replace function
    
    headers = {
        'Authorization' : 'Bearer {token}'.format(token=os.getenv('GENIUS_ACCESS_TOKEN'))
    }
    
    lyric_data = requests.get(BASE_URL + '?q=' + song_name, headers=headers)
    lyric_json = lyric_data.json();
    lyric_path=lyric_json['response']['hits'][0]['result']['path']
    
    lyric_link = BASE_LINK_URL + lyric_path
    
    return lyric_link