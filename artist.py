import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import *

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

class Artist:
    """ 
    Artist class 

    json: json dictionary from spotify API 
    name: artist name 
    id: aritst id 
    album: dictionary of the form {(album, year) : [tracks]} with all albums from artist and 
    all songs associated w that album

    """
    def __init__(self, json):
        self.json = json 
        self.name = json["name"]
        self.id = json["id"]
        self.albums = self.get_albums()

    def get_albums(self):
        """
        Returns a dictionary with (album, year) as key and songs as values

        Has the form: {(album, year) : [tracks]}
        """
        album_dict = {}
        albums = sp.artist_albums(self.id, album_type='album')
        for album in albums['items']:
            name = album["name"]
            album_id = album["id"]
            tracks = sp.album_tracks(album_id)['items']
            year = int(album["release_date"][:4])
            if year >= 2000:
                track_names = [track['name'] for track in tracks]
                track_names = list(set(track_names)) # remove dupes 
                album_dict[name,year] = track_names 
        return album_dict

    def printing(self):
        """
        Prints artist information
        """
        print(f"Artist name: {self.name}")
        for album_name in self.albums.keys():
            print(f"Album name: {album_name[0]}")
            print(f"Year released: {album_name[1]}")
            print(f"Album {album_name[0]} tracks: {self.albums[album_name]}\n")
