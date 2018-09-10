from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('Hello world. Welcome to Django!')
    return render(request, 'home.html', {'name' : 'manidhar'})


def namepage(request):
    return HttpResponse('<p>Manidhar</p>')
