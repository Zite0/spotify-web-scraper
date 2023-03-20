from pandas import DataFrame as df
import spotipy
from artist import Artist
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import CLIENT_SECRET, CLIENT_ID

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

def _songInfo(artist,coder_number =0):
    """
    Returns a 2d list of lists of all the songs by a given artist with the following
    information per each individual row: 
    Coder #, Artist,Album Name,Album Year,Song Name,UndocuSongs,Notes (in this order)
    
    Requires that artist be an Artist object. 
    """

    assert isinstance(artist,Artist)

    songInfo = []
    innerList = []

    albums = artist.albums

    albumKeys = list(albums.keys())
    albumKeys.reverse()

    for key in albumKeys:
        for track in albums[key]:
            innerList.append(coder_number)
            innerList.append(artist.name)
            innerList.append(key[0])
            innerList.append(key[1])
            innerList.append(track)
            innerList.append('')
            innerList.append('')

            songInfo.append(innerList)
            innerList = []
    

    return songInfo


def spotify_csv(artist, coder_number=0):
    """
    Returns a CSV file with an artist's songs and albums, given an Artist instance.
    Parameter artist: instance of Artist (must be an Artist object)
    Parameter coder_number: coder number to put in spreadsheet (must be an int)
    """

    name = artist.name

    csvColumns = ['Coder #','Artist','Album Name','Album Year','Song Name','UndocuSongs?','Notes']

    data = _songInfo(artist=artist,coder_number=coder_number)

    artistframe = df(data=data,columns= csvColumns)

    csvName = name + '.xlsx'
    artistframe.to_excel(csvName,index=False)

    return artistframe

def artistAlbums(artist_name):
    """
    Returns a CSV file with an artist's songs and albums, given an artist's name.
    Parameter artist: artist name as a string
    """