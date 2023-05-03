import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import *
from artist import Artist
from toCsv import * 
import multiprocessing

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

def to_artist(artist_info):
    return Artist(artist_info)


"""
Takes a list of artist names and returns a list of Artist objects.

Precondition: Requires that myList be a list of Strings with 
names of artists.
"""
def artistCreator(myList):

    artistList = []

    for artist in myList:
        result = sp.search(q=artist,type='artist')
        myArtist = Artist(result['artists']['items'][0])
        artistList.append(myArtist)

    return artistList