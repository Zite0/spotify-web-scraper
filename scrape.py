import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='936004f3ef804d04b78af09dbbcd8357',client_secret='56f682b2a40b4bb1b645cd2030271a49'))

uri = 'spotify:artist:7Ln80lUS6He07XvHI8qqHH'

results = spotify.artist_albums(uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])