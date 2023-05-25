from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


import toCsv
import artistCreator

@csrf_exempt
def index(request):
    if request.POST:
        number = request.POST['number'].strip()
        artist = request.POST['artist'].strip()

        if number == '':
            context = {
            'number_feedback': '',
            'artist_feedback': 'hidden',
            'num_artists': 'hidden',
            'sticky_number': number,
            'sticky_artist': artist,
            'display_form': '',
            'display_confirm': 'hidden',
            }

        if artist == '':
            context = {
            'number_feedback': 'hidden',
            'artist_feedback': '',
            'num_artists': 'hidden',
            'sticky_number': number,
            'sticky_artist': artist,
            'display_form': '',
            'display_confirm': 'hidden',
            }

        if number == '' and artist == '':
            context = {
            'number_feedback': '',
            'artist_feedback': '',
            'num_artists': 'hidden',
            'display_form': '',
            'display_confirm': 'hidden',
            }

        if artist.count(',') > 2:
            context = {
            'number_feedback': 'hidden',
            'artist_feedback': 'hidden',
            'num_artists': '',
            'sticky_number': number,
            'sticky_artist': artist,
            'display_form': '',
            'display_confirm': 'hidden',
            }

        if number != '' and artist != '' and artist.count(',') <= 2: #form is valid
            context = {
            'display_form': 'hidden',
            'display_confirm': '',
            'number': request.POST['number'],
            'artist': request.POST['artist'],
            }
        
            artist_lst = toList(request.POST['artist'])

            # Slow: try to fix this crap (added by Zite0).
            while "" in artist_lst:
                artist_lst.remove("")

            artist_objects = artistCreator.artistCreator(artist_lst)
            render(request, 'index.html', context)
            return excelArtist(artist_objects, number)

    else:
        context = {
        'display_form': '',
        'display_confirm': 'hidden',
        'number_feedback': 'hidden',
        'artist_feedback': 'hidden',
        'num_artists': 'hidden',
        }
    return render(request, 'index.html', context)


def excelArtist(artist_objects, number):
    """
    Given a list of artist objects and a coder number, returns a .xlsx file of artist albums and songs.
    """
    toCsv.spotify_csv(artist_objects,'spreadsheets/artists',number)
    with open('spreadsheets/artists.xlsx', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = 'inline; filename=artists'
        return response


def toList(str):
    """
    Takes a string separated by commas and returns a list.
    Requires that `str` is a string.
    """
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


def error404(request):
    return render(request, '404.html')

            
