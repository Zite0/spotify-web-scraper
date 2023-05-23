from toCsv import *
from artist import *
from credentials import *
from artistCreator import *

myList = artistCreator(['artic monkeys'])

monkey = myList[0]

spotify_csv(myList, 'monke')

