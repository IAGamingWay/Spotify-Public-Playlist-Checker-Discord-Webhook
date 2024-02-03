import time
import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
DISCORD_WEBHOOK_URL = 'your_discord_webhook'

sp = Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

spotify_user_id = 'spotify_profile_id'

def get_public_playlists(user_id):
    playlists = sp.user_playlists(user_id)
    public_playlists = [playlist['id'] for playlist in playlists['items'] if playlist['public']]
    return public_playlists

def send_discord_notification(playlist_name, playlist_url):
    payload = {
        "content": f"New Playlist: {playlist_name}\n[gamimeno lig]({playlist_url})"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload, headers=headers)
    if response.status_code != 204:
        print(f"Error: {response.status_code} - {response.text}")

def main():
    previous_playlists = set()

    while True:
        try:
            current_playlists = set(get_public_playlists(spotify_user_id))

            new_playlists = current_playlists - previous_playlists
            if new_playlists:
                for playlist_id in new_playlists:
                    playlist_info = sp.playlist(playlist_id)
                    playlist_name = playlist_info['name']
                    playlist_url = playlist_info['external_urls']['spotify']
                    send_discord_notification(playlist_name, playlist_url)

                previous_playlists = current_playlists

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(3600)

if __name__ == "__main__":
    main()
