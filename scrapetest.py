import toCsv
from introcs import assert_equals
import artist
from pandas import DataFrame as df
import spotipy
import artist
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import CLIENT_SECRET, CLIENT_ID

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

result = sp.search(q = 'Queen', type = 'artist')
artists = result["artists"]["items"]
artist = artist.Artist(artists[0])

path1 = r'C:\Users\luis2\OneDrive\Documentos\GitHub\spotify-web-scraper\spreadsheets\\'


y = toCsv.spotify_csv(artist=artist,coder_number = 4,path=path1)