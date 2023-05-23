from toCsv import *
from artist import *
from credentials import *
from main2 import *

myList = artistCreator(['artic monkeys'])

monkey = myList[0]

spotify_csv(myList, 'monke')

