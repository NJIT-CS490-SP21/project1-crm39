import requests
import os
from dotenv import load_dotenv, find_dotenv

BASE_URL = 'https://api.genius.com/search'

load_dotenv(find_dotenv())

def get_lyrics():
    
    #auth_response  = requests.get()
    print('Hi')
    
    headers = {
        'Authorization' : 'Bearer {token}'.format(token=os.getenv('GENIUS_ACCESS_TOKEN'))
    }
    
    lyric_data = requests.get(BASE_URL + '?q=Stranger%20Things', headers=headers)
    lyric_json = lyric_data.json();
    lyric_path=lyric_json['response']['hits'][0]['result']['path']
    
    print(lyric_path)
    lyric_link = BASE_URL + lyric_path
    print(lyric_link)