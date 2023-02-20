import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='936004f3ef804d04b78af09dbbcd8357',client_secret='56f682b2a40b4bb1b645cd2030271a49'))

def albums(url):
    """
    Returns the album names of a certain artist, given the artist's URL
    Parameter url: URL of artist, given as a string
    Preconditions: must be a valid URL, must be a string
    """
    assert isinstance(url, str)
    assert 'https://open.spotify.com/artist/' in url

    # convert URL to URI
    length = len('https://open.spotify.com/artist/')
    uri = url[length:]

    results = spotify.artist_albums(uri, album_type='album')
    albums = results['items']

    # check for more results
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        albumlist = album['name']

    return remove_dups(albumlist)

def remove_dups(lst):
    """
    Returns a copy of the list with all occurrences of duplicate removed 
    (except for first instance)
    Parameter lst: must be a non-nested list
    """
    assert isinstance(lst, list)

    copylist = []
    for item in lst:
        if item not in copylist:
            copylist.append(item)

    return copylist
    