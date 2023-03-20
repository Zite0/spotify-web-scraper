import toCsv
from introcs import assert_equals
import artist
from pandas import DataFrame as df
import spotipy
import artist
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import CLIENT_SECRET, CLIENT_ID

toCsv.spotify_csv('Arctic Monkeys',coder_number = 4)