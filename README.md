
# Spotify Playlist Importer

I decided to switch my primary streaming platform from Spotify to YouTube Music due to better pricing and a more expansive music library. Due to the number of playlists I created, I knew it would be better to automate the transfer rather than doing creating new playlists all manually. I found no tool that did this the way I wanted, prompting me to develop one myself. 


## Windows Install        

1. Install Python interpreter  
https://www.python.org/downloads/
2. Install git  
https://git-scm.com/download/win

4. Open git-bash and type:    
```bash
git clone https://github.com/lmaqungo/Spotify-Playlist-Importer.git
cd Spotify-Playlist-Importer
python main.py
```

## Usage

Upon running 'main.py', you will be met with this main menu screen:

<img src="https://github.com/lmaqungo/Spotify-Playlist-Importer/blob/main/main%20menu.png?raw=true" alt = "main menu display" width="320">

1. Selecting **_A_** will fetch the playlists from Spotify, and is necessary to select first to enable transferring to YouTube
2. Selecting **_E_** will first prompt you to specify which playlists you would like to transfer for that particular session. Then for each playlist, the YouTube API will search for each track in the playlist, then will prompt the user to confirm the correct video to add to the playlist, as YouTube will often have numerous versions of a particular song from different(unofficial) uploaders.
3. Selecting **_Q_** will quit from the session


## Review

**Technologies**: Python, Spotify API, YouTube API 
**Learnings**: http requests, api usage 
