import toCsv
import artist
from introcs import assert_equals
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import *

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

result = sp.search(q = 'Arctic Monkeys', type = 'artist')
artists = result["artists"]["items"]
artist = artist.Artist(artists[0])
#print(artist.songs())
print(artist.songs().keys())