# Setup

## Install
```bash
    pip3 install -r requirements.txt
```

## Setup api tokens

### Youtube music
Run the following command in the terminal and follow the instructions
```bash
   ytmusicapi oauth
```
and then name the file `youtube_auth.json` and place it in the root directory of the project

### Spotify
Visit [this link](https://developer.spotify.com/dashboard/applications) and create a new app. Then copy the client id and client secret into a file called .env in the root directory of the project like so:
```bash
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret
    SPOTIPY_REDIRECT_URI='http://localhost'
    USERNAME=your_username
```

Tip: You can find your username by going to your spotify profile and clicking the three dots next to your profile picture and then clicking share and copying the link. Your username is the string of numbers and letters after the last slash.

## Run
```bash
    python3 main.py
```

Disclaimer: 
This project is not affiliated with Spotify or Youtube Music in any way.
And Github Copilot was used to generate to write this repository.