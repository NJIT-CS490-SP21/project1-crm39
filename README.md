# Project Name TBD
This usually takes me a while

## Deployment

- Download the following:
    * heroku
    * flask
    * python-dotenv
    * requests
- Clone this repo
- Setup for API requests (local):
    * Get the client id and client secret from the spotify API
    * Get an access token from the genius API
    * Add all three to a .env file (Include this file in your .gitignore)
- Heroku:
    * Create an account if you haven't already
    * Confirm that you have the requirements.txt file containing "Flask", "requests", and "python-dotenv"
    * Confirm that you have a Procfile containing ```web: python app.py```
    * In your terminal use ```heroku login -i``` and sign in
    * Use ```git push heroku [master | main]```
    * View your project in heroku and update the config vars with the variables in the local .env file
    * Use ```heroku open``` or open the app from the Heroku dashboard

## Technical Issues

My biggest roadblock was parsing the json returned by the Spotify API. It was confusing 
to see so many elements nested in dictionaries and lists. I used [CodeBeautify's](https://codebeautify.org/jsonviewer)
jsonviewer to help better visualize the json element and get the necessary values<br><br>

I wasn't sure if I needed to provide the client id and client secret for the genius api get request. 
I searched around to see examples of people using the credentials and ended up finding someone that mentioned
they used the access token provided by genius in their api-clients page
 

## Known problems

- Size of the grid boxes changes depending on the artist
- Haven't figured out how to load the artist name in an h1 tag yet

## Improvements
- I will allow the user to search for the artist
- Create logic to remove the audio player if there is no preview_url provided for the song
- Style the image to improve it's looks (rounded corners, increase size, etc)

## Tools & Technologies
- AWS Cloud9
- Python 3.6.12
- Flask 1.1.12
- HTML/CSS
- Git
- Heroku

## Libraries
- random
- flask
- dotenv
- os
- requests