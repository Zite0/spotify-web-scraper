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

        if number != '' and artist != '':
            context = {
            'display_form': 'hidden',
            'display_confirm': '',
            'number': request.POST['number'],
            'artist': request.POST['artist'],
            }

    else:
        context = {
        'display_form': '',
        'display_confirm': 'hidden',
        'number_feedback': 'hidden',
        'artist_feedback': 'hidden',
        }
    return render(request, 'index.html', context)