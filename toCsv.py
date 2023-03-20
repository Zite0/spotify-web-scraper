from pandas import DataFrame as df
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import CLIENT_SECRET, CLIENT_ID

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

def spotify_csv(artist, coder_number):
    """
    Returns a CSV file with an artist's songs and albums, given the artist's URL.
    Parameter url: URL of artist, given as a string
    Preconditions: must be a valid URL, must be a string
    """

    name = artist.name
    albums = artist.albums # dictionary of format {(album_name, year): [song list]} -> all albums from artist 

    csvColumns = ['Coder #','Artist','Album Name','Album Year','Song Name','UndocuSongs?','Notes']
    data = {[]}

    artistdict = [coder_number, name, albums.values, albums.keys]
    artistframe = df(data=artistdict,columns=['Song Name'])

    csvName = name + '.csv'

    return artistframe.to_csv(csvName)
    