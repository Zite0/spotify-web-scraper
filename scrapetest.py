import toCsv
from introcs import assert_equals
import artist
from pandas import DataFrame as df
import spotipy
import artist
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import CLIENT_SECRET, CLIENT_ID

#spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

# Test remove_dups

#lst1 = ['a','b','c','d','a']
#lst2 = ['a','b','c','d']
#assert_equals(lst2,scrape.remove_dups(lst1))

#lst1 = ['b','b','b','b']
#lst2 = ['b']
#assert_equals(lst2,scrape.remove_dups(lst1))

#lst1 = ['aab','ttt','aab','aab']
#lst2 = ['aab','ttt']
#assert_equals(lst2,scrape.remove_dups(lst1))

#lst1 = [1,2,3,4,44,44]
#lst2 = [1,2,3,4,44]
#assert_equals(lst2,scrape.remove_dups(lst1))

#lst1 = [1,1,1,1]
#lst2 = [1]
#assert_equals(lst2,scrape.remove_dups(lst1))

#print(scrape.songs('https://open.spotify.com/artist/7Ln80lUS6He07XvHI8qqHH'))
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))

result = sp.search(q = 'Red Hot Chili Peppers', type = 'artist')
artists = result["artists"]["items"]
artist = artist.Artist(artists[0])
songs = artist.get_album_songs('Return of the Dream Canteen')
print(songs)




y = toCsv.spotify_csv(artist=artist,coder_number = 4)
##print(y)


#toCsv.spotify_csv('https://open.spotify.com/artist/7Ln80lUS6He07XvHI8qqHH')