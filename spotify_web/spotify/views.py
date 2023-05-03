from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import redirect

import toCsv
import main2
import time

def index(request):
    if request.POST:
        number = request.POST['number'].strip()
        artist = request.POST['artist'].strip()

        if number == '':
            context = {
            'number_feedback': '',
            'artist_feedback': 'hidden',
            'sticky_number': number,
            'sticky_artist': artist,
            'display_form': '',
            'display_confirm': 'hidden',
            }

        if artist == '':
            context = {
            'number_feedback': 'hidden',
            'artist_feedback': '',
            'sticky_number': number,
            'sticky_artist': artist,
            'display_form': '',
            'display_confirm': 'hidden',
            }

        if number == '' and artist == '':
            context = {
            'number_feedback': '',
            'artist_feedback': '',
            'display_form': '',
            'display_confirm': 'hidden',
            }

        if number != '' and artist != '': #form is valid
            context = {
            'display_form': 'hidden',
            'display_confirm': '',
            'number': request.POST['number'],
            'artist': request.POST['artist'],
            }
        
            artist_lst = toList(request.POST['artist'])
            artist_objects = main2.artistCreator(artist_lst)
            return excelArtist(artist_objects, number)

    else:
        context = {
        'display_form': '',
        'display_confirm': 'hidden',
        'number_feedback': 'hidden',
        'artist_feedback': 'hidden',
        }
    return render(request, 'index.html', context)

"""
Given a list of artist objects and a coder number, returns a .xlsx file of artist albums and songs.
"""
def excelArtist(artist_objects, number):
    toCsv.spotify_csv(artist_objects,'spreadsheets/artists',number)
    with open('spreadsheets/artists.xlsx', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = 'inline; filename=artists'
        return response

"""
Takes a string separated by commas and returns a list.
Requires that `str` is a string.
"""
def toList(str):
    if ',' not in str:
        return [str]
    else:
        pos = str.index(',')
        artists = [str[:pos].strip()]
        while ',' in str[pos:]:
            one = str.index(',',pos)+1
            if ',' in str[one:]:
                two = str.index(',',one)
                artists.append(str[one:two].strip())
                pos = two
            else:
                artists.append(str[one:].strip())
                pos = one
        return artists
            
