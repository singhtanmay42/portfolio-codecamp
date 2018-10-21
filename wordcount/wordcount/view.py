from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
def eggs(request):
    return HttpResponse('<h1>EGGS</h1>')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    char = 0
    for words in wordlist:
        for char in words:
            char = char + 1
        avgnum = char/len(wordlist)
    return render(request,'count.html',{'fulltext':fulltext,'count': len(wordlist),'avgnum' : avgnum})
