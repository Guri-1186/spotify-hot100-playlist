import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{user_input}"

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

song_uris = []
year = user_input.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f"Billboard Hot 100 - {user_input}"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

if song_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    print(f"Playlist '{playlist_name}' created successfully with {len(song_uris)} songs!")
else:
    print("No songs were found on Spotify.")