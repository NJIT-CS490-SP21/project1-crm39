from flask import Flask, render_template
from spotify import get_songs
import os

app = Flask(__name__)

@app.route('/')
def main_page():
    songs = get_songs()
    
    return render_template(
        'index.html',
        len = len(songs),
        songs = songs
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)