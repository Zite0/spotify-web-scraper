from pandas import DataFrame as df
import spotipy
from artist import Artist
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import CLIENT_SECRET, CLIENT_ID

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))


def _songInfo(artist, coder_number=0):
    """
    Returns a 2d list of lists of all the songs by a given artist with the following
    information per each individual row: 
    Coder #, Artist,Album Name,Album Year,Song Name,UndocuSongs,Notes (in this order)
    
    Requires that artist be an Artist object. 
    """

    songInfo = []

    albums = artist.albums

    albumKeys = list(albums.keys())
    albumKeys.reverse()

    for key in albumKeys:
        for track in albums[key]:
            innerList = [coder_number, artist.name, key[0], key[1], track, "", ""]

            songInfo.append(innerList)

    return songInfo


def spotify_csv(artist_lst: list, file_name: str, coder_number=0):
    """
    Returns a xlsx file with an artist's songs and albums, given an artist's name.
    Parameter artist_lst: list of Artist objects
    Parameter file_name: name of the xlsx file
    Parameter coder_number: coder number to put in spreadsheet (must be an int; default is zero)
    """
    data = []

    for artist in artist_lst:
        new_data = _songInfo(artist=artist, coder_number=coder_number)
        data += new_data

    csvColumns = ['Coder #', 'Artist', 'Album Name', 'Album Year', 'Song Name', 'UndocuSongs?', 'Notes']

    artistFrame = df(data=data, columns=csvColumns)

    csvName = file_name + '.xlsx'
    artistFrame.to_excel(csvName, index=False)


