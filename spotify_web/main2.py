import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import *
from artist import Artist
from toCsv import * 
import multiprocessing

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

def to_artist(artist_info):
    return Artist(artist_info)


"""
Takes a list of artist names and returns a list of Artist objects.

Precondition: Requires that myList be a list of Strings with 
names of artists.
"""
def artistCreator(myList):

    artistList = []

    for artist in myList:
        result = sp.search(q=artist,type='artist')
        myArtist = Artist(result['artists']['items'][0])
        artistList.append(myArtist)

    return artistList


        
    


def main():
    artist_name_list = []
    coder_number = 0
    file_name = ""

    while 1:
        file_name = input("What do you want to name your file?\n")
        if file_name == "" or file_name.isspace():
            print("Invalid file name. Please try again.\n")
            continue 
        selection = input(f"Did you mean file name {file_name}? Type 'Yes' or 'No'.\n")
        while selection.upper() not in ['YES', 'NO']:
            selection = input(f"Did you mean file name {file_name}? Type 'Yes' or 'No'.\n")
        if (selection.upper() == 'YES'):
            break 
        else:
            continue 

    while 1:
        coder_number = input("Input your coder number.\n")
        if not coder_number.isnumeric():
            print("Invalid coder number. Please try again.\n")
            continue 
        coder_number = int(coder_number)
        selection = input(f"Did you mean number {coder_number}? Type 'Yes' or 'No'.\n")
        while selection.upper() not in ['YES', 'NO']:
            selection = input(f"Did you mean number {coder_number}? Type 'Yes' or 'No'.\n")
        if (selection.upper() == 'YES'):
            break 
        else:
            continue 

    while 1:
        user_input = input("Please write artist name. Type 'QUIT' to exit program.\n")
        if user_input.upper() == "QUIT":
            break
        if user_input.upper() == "" or user_input.isspace():
            print("Invalid artist. Please try again.")
            continue
        result = sp.search(q = user_input, type = "artist")
        # print(result) # -> print this to view json string 
        artists = result["artists"]["items"]
        if len(artists) == 0:
            print("Invalid artist. Please try again.")
            continue
        selection = input(f"Did you mean: {artists[0]['name']}? Type 'Yes' or 'No'.\n")
        while selection.upper() not in ['YES', 'NO']:
            selection = input(f"Did you mean: {artists[0]['name']}? Type 'Yes' or 'No'.\n")
        if (selection.upper() == 'YES'):
            artist_name_list.append(artists[0])
        else:
            continue

    pool = multiprocessing.Pool()
    result = pool.map(to_artist, artist_name_list)

    spotify_csv(result, file_name, coder_number)