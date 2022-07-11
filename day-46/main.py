import requests
import spotipy
from spotipy.oauth2 import SpotifyStateError, SpotifyOAuth, SpotifyClientCredentials
from bs4 import BeautifulSoup


#Client details
CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR CLIENT SECRET"

#Getting top  100 songs on billboard on specified date
choice_of_year = input(f"Which year do you want to travel to?Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{choice_of_year}/"
response = requests.get(URL)
website_info = response.text

soup = BeautifulSoup(website_info, features="html.parser")
song_title = soup.find_all("li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direct"
                                          "ion-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-"
                                          "max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")

song_titles = [song.getText().strip().replace("\n","").replace("\t",",") for song in song_title]


#Creating private playlist
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))
user = sp.current_user()["id"]


# Initialize spotify search API

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

song_uris=[]
year=choice_of_year.split("-")[0]

for details in song_titles:
    title_of_song = details.split(",", 2)[0]
    results = sp.search(q=f'track:' + title_of_song, type='track')
    items = results['tracks']['items']
    if len(items) > 0:
        song_detail= items[0]
        song_uri = (song_detail['uri'])
        song_uris.append(song_uri)
    else:
        print(f"{title_of_song} doesn't exist in Spotify. Skipped.")

#Adding to playlist
playlist = sp.user_playlist_create(user=user, name=f"{year} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
