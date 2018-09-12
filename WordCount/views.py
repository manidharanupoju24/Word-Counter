from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('Hello world. Welcome to Django!')
    return render(request, 'home.html')


def countpage(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_count = len(word_list)

    return render(request, 'count.html', {'fulltext': fulltext, 'word_list': word_list, 'word_count': word_count})
