# Project 1
This demo explains how to call the Spotify API and Genius API using the Python requests libary and parse its JSON data on cloud9 services on aws

---

## Requirements
1. `pip install Flask`
2. `pip install python-detenv`
3. `pip install requests`

## Setup

#### Open-source libraries used
- Spotify Web API (https://developer.spotify.com/documentation/web-api/quick-start/) - Simple HTTP requests with JSON parsing
- Genius API (https://docs.genius.com/#/getting-started-h1)

#### Store and hide your API keys with a .env file and .gitignore file, respectively
1. Create .env file in your main directory
2. Add Spotify Client Id and Client Secret from https://developer.spotify.com/dashboard/applications and Genius Token with the lines:
    * `export SPOTIFY_ID='YOUR_ID'`
    * `export SPOTIFT_SECRET='YOUR_SECRET'`
    * `export GENIUS_ACCESS_TOKEN`
3. Create .gitignore file in your main directory and add `.env` to the file
    * this will avoid pusing the .env file on remote git reponsitory


## Run Application
1. Run command in terminal `python main.py`
2. Preview web page in browser '/'

---
## Notes
### Known Problem
- There are no known problems with the Web Applcation.

### Additional Features that I might implement
- I would like to make my web application reponsive so that the web application automatically adjust and adapt to any screen size. I would to implementing that in the css file using a media query to add a breakpoint from diffrent screen sizes.
  
### Technical Difficulties
- While working on this project, a techical difficulty that I encountered was that after making changes to css file, the change would not get updated on preview. When I renamed the css file and provided new css file path, it worked but it is very inconvient to do that each time. In order to solve this problem, I used this line of code: APP.CONFIG['SEND_FILE_MAX_AGE_DEFAULT'] = 0 in the python file. For me, even that did not solve the problem so I have to clear my browser cache file everytime in order to see the changes made in css file reflacted in the preview window.
- Another problem that I encontered was parsing the JSON data correcty. To fix this issue, I formatted JSON data using this line:     json_formatted_str = json.dumps(data, indent=2) and stored the data in another file to see it better. Another helpful tool that I found which serching for solution is https://jsonformatter.curiousconcept.com/#


