from pandas import DataFrame as df
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='936004f3ef804d04b78af09dbbcd8357',client_secret='56f682b2a40b4bb1b645cd2030271a49'))

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

def songs(url):
    """
    Returns the songs of an artist's albums in a dictionary format.
    Keys are albums, values are song lists.
    Parameter url: URL of artist, given as a string
    Preconditions: must be a valid URL, must be a string
    """

    album_dict = albums(url)
    song_dict = {}

    for album_id in album_dict:
        results = spotify.album_tracks(album_id)
        songs = results['items']

        # check for more results
        while results['next']:
            results = spotify.next(results)
            songs.extend(results['items'])

        songlist = []
        for song in songs:
            songlist.append(song['name'])

        song_dict[album_dict[album_id]] = songlist

    return song_dict

def spotify_csv(url):
    """
    Returns a CSV file with an artist's songs and albums, given the artist's URL.
    Parameter url: URL of artist, given as a string
    Preconditions: must be a valid URL, must be a string
    """

    data = songs(url)

    albumlist = []
    songlist = []
    for name in data:
        albumlist.append(name)
        songlist.append(data[name])

    artistframe = df(songlist).transpose()
    artistframe.columns = albumlist

    # get artist name
    uri = uri_to_url(url)
    artist_data = spotify.artist(uri)
    artist = artist_data['name']
    csvName = str(artist) + '.csv'

    return artistframe.to_csv(csvName)
    