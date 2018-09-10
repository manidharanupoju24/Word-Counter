from django.http import HttpResponse


def homepage(request):
    return HttpResponse('Hello world. Welcome to Django!')


def namepage(request):
    return HttpResponse('<p>Manidhar</p>')
