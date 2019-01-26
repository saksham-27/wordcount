from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, 'home.html')


def count(request):
    data=request.GET['fulltextarea']
    print(data)
    words=data.split()
    worddictionary={}
    l=len(words)
    for word in words:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    return render(request, 'count.html',{'worddictionary':worddictionary.items(),'l':l,'fulltext':data,'words': words})
def about(request):
    return render(request,'about.html')
