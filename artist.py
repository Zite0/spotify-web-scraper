import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='936004f3ef804d04b78af09dbbcd8357',client_secret='56f682b2a40b4bb1b645cd2030271a49'))

class Artist:
    """ 
    Artitst class 
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
