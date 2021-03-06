import requests
import os
from dotenv import load_dotenv, find_dotenv
import random
import json
from flask import Flask, render_template

app = Flask(__name__)
# sets the cache control max age to this number of seconds.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def homepage():
    
    #spotify
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    load_dotenv(find_dotenv())
    
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
    #creates random number
    lenTrack = len(data['tracks'])
    
    if lenTrack == 0:
        songName = "Thinking out Loud"
        songArtist = "Ed Sheeran"
        songImageURL  = "https://i.scdn.co/image/ab67616d00001e02d08209944468440145f01524"
        songPreviewURL = "https://p.scdn.co/mp3-preview/cec1fc40a0220f20d3b91dd28d8e1141ad5e7e25?cid=0b1c2b0f0b974fff84db76a4244457f8"
    else:
        randA=random.randint(0,lenTrack-1)
        songName = data['tracks'][randA]['name']
        songArtist = data['tracks'][randA]['artists'][0]['name']
        songImageURL =data['tracks'][randA]['album']['images'][1]['url']
        songPreviewURL = data['tracks'][randA]['preview_url']
    
    
    #Genius
    geniusAccessToken= os.getenv('GENIUS_ACCESS_TOKEN')
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + geniusAccessToken}
    search_url = base_url + '/search'
    data = {'q': songName + ' ' + songArtist}
    response = requests.get(
        search_url, 
        data=data, 
        headers=headers
        )
    dataFromGenius = response.json()
    
    '''
    json_formatted_str = json.dumps(dataFromGenius, indent=2)
    f = open("data.txt","w+")
    f.write(json_formatted_str)
    '''
    
    lyrics = dataFromGenius['response']['hits'][0]['result']['url']
    
    return render_template(
        'index.html',
        songName=songName,
        songArtist=songArtist,
        songImageURLS=songImageURL,
        songPreviewURLS=songPreviewURL,
        lyricsURL = lyrics
        )
    
app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv("IP", '0.0.0.0'),
    use_reloader=True,
    debug  = True #dont have keep closing and restarting server when we make change (restart the server)
    )