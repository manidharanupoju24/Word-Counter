from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    # return HttpResponse('Hello world. Welcome to Django!')
    return render(request, 'home.html')


def countpage(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    count = len(word_list)

    wordDict = {}

    for word in word_list:
        if word in wordDict:
            # increment
            wordDict[word] += 1
        else:
            # Add to the dict
            wordDict[word] = 1

    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'word_list': word_list, 'count': count,
                                          'wordDict': sortedWords})
