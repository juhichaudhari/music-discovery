import requests
import os
from dotenv import load_dotenv, find_dotenv
import random
import json

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
#ed shareen, ariana granda, taylor swift
artistIDs = ['6eUKZXaKkcviH0Ku9w2n3V', '66CXWjxzNUsdJxJ2JdwvnR', '06HL4z0CvFAxyc27GXpf02', '4YRxDV8wJFPHPTeXepOstw']
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

#first index 0 is for the album
songName = data["tracks"][0]["name"]
songArtist = data["tracks"][0]["artists"][0]["name"]
songImage = ""
songPreviewURL = ""

print("song: ", songName)
print("antist: ", songArtist)
#print(SongImage)
print(songPreviewURL)

#print(data)