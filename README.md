# Project Name TBD
This usually takes me a while

## Technical Issues

My biggest roadblock was parsing the json returned by the Spotify API. It was confusing 
to see so many elements nested in dictionaries and lists. I used [CodeBeautify's](https://codebeautify.org/jsonviewer)
jsonviewer to help better visualize the json element and get the necessary values.<br><br>

I wasn't sure if I needed to provide the client id and client secret for the genius api get request. 
I searched around to see examples of people using the credentials and ended up finding someone that mentioned
they used the access token provided by genius in their api-clients page.
 

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
- HTML
- Git

## Libraries
- random
- flask
- dotenv
- os
- requests