import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import *
from artist import Artist
from toCsv import * 

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

artists_list = []
coder_number = 0

while 1:
    coder_number = input("Input your coder number. ")
    if type(int(coder_number)) != int:
        print("Invalid coder number. Please try again. ")
        continue 
    coder_number = int(coder_number)
    user_input = input("Please write artist name. Type 'QUIT' to exit program.\n")
    if user_input.upper() == "QUIT":
        break
    if user_input.upper() == "" or user_input.isspace():
        print("Invalid artist. Please try again.")
        continue
    result = sp.search(q = user_input, type = "artist")
    print(result)
    artists = result["artists"]["items"]
    if len(artists) == 0:
        print("Invalid artist. Please try again.")
        continue
    selection = input(f"Did you mean: {artists[0]['name']}? Type 'Yes' or 'No'.\n")
    while selection.upper() not in ['YES', 'NO']:
        selection = input(f"Did you mean: {artists[0]['name']}? Type 'Yes' or 'No'.\n")
    if (selection.upper() == 'YES'):
        artist = Artist(artists[0])
        artists_list.append(artist)
    else:
        continue


for artist in artists_list:
        spotify_csv(artist, coder_number)

# if __name__ == '__main__':
# 	main()