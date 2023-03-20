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

    def albumDict(self):
        """
        Returns the album names of a certain artist as a dictionary, given the artist's URL.
        Keys are IDs, values are album names.

        Parameter url: URL of artist, given as a string
        Preconditions: must be a valid URL, must be a string
        """

        results = sp.artist_albums(self.id, album_type='album',country='US')
        albums = results['items']

        # check for more results
        while results['next']:
            results = sp.next(results)
            albums.extend(results['items'])

        # add album names to dictionary with IDs
        album_dict = {}
        for album in albums:
            album_dict[album['id']] = album['name']

        self.remove_dict_dups(album_dict)

        return(album_dict)
    
    def remove_dict_dups(self,d):
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

    
    def songs(self):
        """
        Returns the songs of an artist's albums in a dictionary format.
        Keys are albums, values are song lists.
        Parameter url: URL of artist, given as a string
        Preconditions: must be a valid URL, must be a string
        """
        album_dict = self.albumDict()
        song_dict = {}

        for album_id in album_dict:
            results = sp.album_tracks(album_id)
            songs = results['items']

            # check for more results
            while results['next']:
                results = sp.next(results)
                songs.extend(results['items'])

            songlist = []
            for song in songs:
                songlist.append(song['name'])

            song_dict[album_dict[album_id]] = songlist

        return song_dict

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
        Returns if album is not found (invalid album name)

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
        Returns empty list if album is not found (invalid album name)

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
