import requests
import json

def generate_api_token():
    client_id = "c6336ff57cac46ec8deb5edeab25e9b5"
    client_secret = "143cbfe118744abd8e16b8be07aec477"
    url = "https://accounts.spotify.com/api/token"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    } 
    data = {
    "grant_type": "client_credentials",
    "client_id": f"{client_id}",
    "client_secret": f"{client_secret}"
    }  
    
    api_token = json.loads(requests.post(url, headers=headers, data=data).text)["access_token"]
    
    return api_token

def fetch_playlists(accessToken): 

    url = "https://api.spotify.com/v1/users/a3icqjn37ong3uuy2j53wy2bj/playlists"

    headers = {
        "Authorization": f"Bearer {accessToken}"
    }

    my_playlists = json.loads(requests.get(url, headers=headers).text)["items"]
    
    playlist_dict = {}
    
    for playlist in my_playlists:
        playlist_name = playlist["name"]
        playlist_id = playlist["id"]
        playlist_dict[playlist_name] = playlist_id
    
    # return dictionary in the form of "playlistName" : "playlistId"

    return playlist_dict

def fetch_playlist_tracks(accessToken, playListID:str):
    
    url = f"https://api.spotify.com/v1/playlists/{playListID}?fields=tracks.items%28track%28name%2C+artists%28name%29%29%29"
    
    headers = {
        "Authorization": f"Bearer {accessToken}"
    }
    
    playlist = json.loads(requests.get(url, headers=headers).text)["tracks"]["items"]
    tracks = []
    for track in playlist:
        artists = [artist["name"] for artist in track["track"]["artists"]]
        name = track["track"]["name"]
        artist_string = ", ".join(artists).strip()
        tracks.append(f"{artist_string} - {name}")
        
    return tracks[::-1]
    
    #returns a list of tracks from the given playlist
    



