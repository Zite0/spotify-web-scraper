import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import *

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

class Artist:
    """ 
    Artist class 

    Represents an individual artist, with the following following attributes:
    - self.json: json dictionary extracted from spotify API 
    - self.name: artist name 
    - self.id: aritst id 
    - self.album: dictionary of the form {(album, year) : [tracks]} with all albums from artist and 
    all songs associated w that album

    """
    def __init__(self, json):
        """
        json: a json dictionary 

        Initializes class Artist. 
        """
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
    
    def get_album_year(self, album_name):
        """
        Returns album's release year given its name.
        Returns if album is not found (invalud album name)

        Parameter album_name: of type string, it's the key of the album you're looking for
        """
        albums = self.albums 
        for (name, year) in albums.keys():
            if name == album_name:
                return year 
            
        return 0
    
    def get_album_songs(self, album_name):
        """
        Returns list of album's songs year given its name.
        Returns empty list if album is not found (invalud album name)

        Parameter album_name: of type string, it's the key of the album you're looking for
        """
        albums = self.albums 
        for album_info in albums.keys():
            if album_info[0] == album_name:
                return albums[album_info]
        
        return []

    def printing(self):
        """
        Prints artist information
        """
        print(f"Artist name: {self.name}")
        for album_name in self.albums.keys():
            print(f"Album name: {album_name[0]}")
            # print(f"Year released: {album_name[1]}")
            print(f"Year released: {self.get_album_year(album_name[0])}")
            # print(f"Album {album_name[0]} tracks: {self.albums[album_name]}\n")
            print(f"Album {album_name[0]} tracks: {self.get_album_songs(album_name[0])}\n")
