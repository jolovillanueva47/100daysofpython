import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID="your_client_id"
CLIENT_SECRET="your_client_secret"

auth_scope="playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://example.com",
                                               scope=auth_scope))

user_id = sp.current_user()["id"]

billboard_url="https://www.billboard.com/charts/hot-100/"
date_input=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year=date_input.split("-")[0]
response=requests.get(f"{billboard_url}{date_input}")
billboard_html=response.text
soup=BeautifulSoup(billboard_html,"html.parser")
songs=soup.select(".chart-element__information__song")
song_list=[song.text for song in songs]

songs_uri_list=[]
for song in song_list:
    query=f"track:{song} year:{year}"
    try:
        queried_song=sp.search(query,limit=1)
        songs_uri_list.append(queried_song["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        continue

playlist_name=f"{date_input} Billboard 100"
playlist=sp.user_playlist_create(user_id, playlist_name, public=False)
playlist_uri=playlist["uri"]
sp.user_playlist_add_tracks(user_id, playlist_uri, songs_uri_list, position=None)
