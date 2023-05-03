from django.shortcuts import render
from django.http import HttpResponse, request

def index(request):
    if request.POST:
        context = {
        'display_form': 'hidden',
        'display_confirm': '',
        'number': request.POST['number'],
        'artist': request.POST['artist'],
        }
        print(request.POST['number'])
        print(request.POST['artist'])
    else:
        context = {
        'display_form': '',
        'display_confirm': 'hidden',
        }
    return render(request, 'index.html', context)