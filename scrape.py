import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='936004f3ef804d04b78af09dbbcd8357',client_secret='56f682b2a40b4bb1b645cd2030271a49'))

album_dict = {}

def albums(url):
    """
    Returns the album names of a certain artist as a list, given the artist's URL.
    Album names are stored in the dictionary `album_dict` based on IDs.

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

    # add album names to dictionary with IDs
    for album in albums:
        album_dict[album['id']] = album['name']

    remove_dict_dups(album_dict)    
    
    return list(album_dict.values())

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
    