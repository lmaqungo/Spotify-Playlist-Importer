import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import google.auth.transport.requests
import pickle

scopes = ["https://www.googleapis.com/auth/youtube.readonly", 
          "https://www.googleapis.com/auth/youtubepartner",
            "https://www.googleapis.com/auth/youtube",
            "https://www.googleapis.com/auth/youtube.force-ssl"
        ]
credentials_file = "auth/auth.pickle"

def load_api():
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "auth/client_secret.json"

    credentials = None

    # Load credentials from file if they exist
    if os.path.exists(credentials_file):
        with open(credentials_file, 'rb') as token:
                credentials = pickle.load(token)
                

    # If there are no (valid) credentials, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(google.auth.transport.requests.Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(credentials_file, 'wb') as token:
            pickle.dump(credentials, token)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    return youtube

# ADDS A VIDEO TO A PLAYLIST. 
# Provide playlistId, videoID and position in the playlist
def add_to_playlist(YouTubeApiObject, playlistId:str, videoId:str, position:int):
    request = YouTubeApiObject.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": playlistId,
            "position": position,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": videoId
            }
          }
        }
    )
    response = request.execute()
    
#CREATING PLAYLISTS
# the 'parts' that you use must match the elements of the body
def create_playlist(YouTubeApiObject, playlistName:str):
    request = YouTubeApiObject.playlists().insert(
        part = 'status, snippet',
        body= {
            "snippet": {
            "title": playlistName
          }, "status": {
        "privacyStatus": "private"
            }
        }
    )
    response = request.execute()
    playlist_id = response["id"]
    #return playlist id

    return playlist_id
    
#SEARCHING YOUTUBE
def search(YouTubeApiObject, searchQuery:str):
    request = YouTubeApiObject.search().list(
        part="snippet",
        maxResults=15,
        order="relevance",
        q=searchQuery,
        type="video",
        videoDuration="medium"
    )
    
    search_results = []
    response = request.execute()["items"]
    for song in response:
        video = song["snippet"]["title"]
        channel = song["snippet"]["channelTitle"]
        video_id = song["id"]["videoId"]
        search_results.append({f"Track:{video}  Channel: {channel}" : video_id})
        
    return search_results
    
    # function will return the search dictionary

#VIEW CONTENTS OF PLAYLIST
def view_playlist(YouTubeApiObject, playlistId:str):
    request = YouTubeApiObject.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=25,
        playlistId=playlistId
    )
    response = request.execute()
    # function must return the playlist name & its contents

    return response
    
    
            
    
    
if __name__ == "__main__":
    youtube = load_api()
    search_res = search(youtube, "Drake Worst Behaviour")
    for res in search_res:
        print(res)
        



