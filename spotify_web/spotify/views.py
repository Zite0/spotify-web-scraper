from django.shortcuts import render
from django.http import HttpResponse, request

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
            print(artist_lst)

    else:
        context = {
        'display_form': '',
        'display_confirm': 'hidden',
        'number_feedback': 'hidden',
        'artist_feedback': 'hidden',
        }
    return render(request, 'index.html', context)

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
            
