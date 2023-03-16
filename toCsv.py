from pandas import DataFrame as df
import spotipy
from artist import Artist
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import CLIENT_SECRET, CLIENT_ID

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

def uri_to_url(url):
    """
    Returns the URI of an artist, given the artist's URL
    
    Parameter url: URL of artist, given as a string
    Preconditions: must be a valid URL, must be a string
    """
    assert isinstance(url, str)
    assert 'https://open.spotify.com/artist/' in url

    # convert URL to URI
    length = len('https://open.spotify.com/artist/')
    uri = url[length:]

    return uri

def albums(url):
    """
    Returns the album names of a certain artist as a dictionary, given the artist's URL.
    Keys are IDs, values are album names.

    Parameter url: URL of artist, given as a string
    Preconditions: must be a valid URL, must be a string
    """
    uri = uri_to_url(url)

    results = spotify.artist_albums(uri, album_type='album')
    albums = results['items']

    # check for more results
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    # add album names to dictionary with IDs
    album_dict = {}
    for album in albums:
        album_dict[album['id']] = album['name']

    remove_dict_dups(album_dict)

    return(album_dict)

def remove_dict_dups(d):
    """
    Modifies the dictionary to remove all occurrences of duplicate 
    (except for first instance)
    Parameter d: must be a dictionary
    """
    assert isinstance(d, dict)

    new_dict = {}
    values = []
    for item in d:
        if d[item] not in values:
            values.append(d[item])
            new_dict[item] = d[item]

    # modify dictionary
    d.clear()
    for val in new_dict:
        d[val] = new_dict[val]



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

    albums = artist.get_albums()

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
    Returns a CSV file with an artist's songs and albums, given the artist's URL.
    Parameter url: URL of artist, given as a string
    Preconditions: must be a valid URL, must be a string
    """

    name = artist.name

    csvColumns = ['Coder #','Artist','Album Name','Album Year','Song Name','UndocuSongs?','Notes']

    data = _songInfo(artist=artist,coder_number=coder_number)

    artistframe = df(data=data,columns= csvColumns)

    csvName = name + '.xlsx'
    artistframe.to_excel(csvName,index=False)

    return artistframe
    