import YouTubeApi as YouTube
import SpotifyApi as Spotify


FetchedPlaylists = {}

def main():
    spotifyToken = Spotify.generate_api_token()
    youtubeApi = YouTube.load_api()
    print("Welcome to the Spotify playlist Importer. ")
    
    while True:
        mode = input(f"\nFetch playlists from Spotify(A)\nImport to YouTube(E)\nQuit(Q)\n").lower().strip()
        if mode == "a":
            global FetchedPlaylists
            if len(FetchedPlaylists) == 0:
                FetchedPlaylists = Spotify.fetch_playlists(spotifyToken)
                print("\nPlaylists found in account:")
                n = 1
                for playlistName in FetchedPlaylists.keys():
                    print(f"{n}. {playlistName}")
                    n+=1
            else:
                print("playlists already fetched")
                
        elif mode == "e":
            desired_playlists_indices = [int(n) for n in input("Indicate the playlists you would like to import in a comma separated list: ").strip().split(",")]
            for indice in desired_playlists_indices:
                desired_playlist_names = list(FetchedPlaylists.keys())
                playlist_name = desired_playlist_names[indice -1]
                spotify_playlist_id = FetchedPlaylists[playlist_name]
                print(f"Now importing: {playlist_name}\n")
                youtube_playlist_id = YouTube.create_playlist(youtubeApi, playlist_name)
                tracks = Spotify.fetch_playlist_tracks(accessToken=spotifyToken, playListID=spotify_playlist_id)
                for track in tracks:
                    track_position = 1
                    print(f"Processing {track}\n...")
                    search_results = YouTube.search(youtubeApi, track)
                    print("This is what YouTube Found: \n")
                    for result in search_results:
                        print(f"{track_position}. {list(result.keys())[0]}")
                        track_position +=1
                    search_index = int(input("\nIndicate which video to add by specifying its order within the list: ").strip()) - 1
                    song_to_add_dict = search_results[search_index]
                    song_title = list(song_to_add_dict.keys())[0]
                    song_video_id = list(song_to_add_dict.values())[0]
                    track_position = 0
                    print(f"\nAdding {song_title}") # FIX THE FORMATTING OF THIS!!!!!
                    YouTube.add_to_playlist(youtubeApi, youtube_playlist_id, song_video_id , track_position)
                    track_position+=1
                print(f"{playlist_name} has been added") 
                resume = int(input("Are you ready to move onto the next playlist? Indicate \'yes\' with a \'1\', or \'no\' with a \'0\': "))
                if resume == 1:
                    continue
                else:
                    break
                
        elif mode == "q":
            print("Thank you for using the system")
            break
        
        else:
            print("Please indicate the correct operation")
            
            
            
if __name__ == "__main__":    
    main()