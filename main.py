import requests
import os
from dotenv import load_dotenv, find_dotenv
import random
import json
from flask import Flask, render_template

#getting access code from file
load_dotenv(find_dotenv())

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('SPOTIFY_ID'),
    'client_secret': os.getenv('SPOTIFY_SECRET'),
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

#Artist ID
#ed sheeran, ariana granda, taylor swift
artistIDs = ['6eUKZXaKkcviH0Ku9w2n3V', '66CXWjxzNUsdJxJ2JdwvnR', '06HL4z0CvFAxyc27GXpf02']
randNum = random.randint(0, len(artistIDs)-1)
randArtist =  artistIDs[randNum]

#url = 'GET https://api.spotify.com/v1/artists/{id}/top-tracks'
url = BASE_URL + 'artists/' + randArtist + '/top-tracks?market=US'
#print(url)

MARKET = 'US'

response = requests.get(
    url,
    headers=headers
    )
    
data = response.json()

json_formatted_str = json.dumps(data, indent=2)
f = open("data.txt","w+")
f.write(json_formatted_str)

#find how many albams
#randomy select an album

#first index 0 is for the album
songName = data['tracks'][0]['name']
songArtist = data['tracks'][0]['artists'][0]['name']
songImageURL =data['tracks'][0]['album']['images'][1]['url']
songPreviewURL = data['tracks'][0]['preview_url']


print("song: ", songName)
print("antist: ", songArtist)
print("Image URL:", songImageURL)
print("preview Url:",songPreviewURL)

#print(data)


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template(
        'index.html',
        someName=songName,
        songArtist=songArtist,
        songImageURLS=songImageURL,
        songPreviewURLS=songPreviewURL
        )
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv("IP", '0.0.0.0'),
    debug  = True #dont have keep closing and restarting server when we make change (restart the server)
    )