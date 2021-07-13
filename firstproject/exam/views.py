from django.shortcuts import render
from django.http import HttpResponse
def showResult(request):
    s='<h1>This is Result Page</h1>'
    return HttpResponse(s)
def showTest(request):
    que='Who developed C Language?'
    a='Ken Thompson'
    b='Dennis Ritchie'
    c='Bjarne Stroustrup'
    d='James Bosling'
    data={'que':que,'a':a,'b':b,'c':c,'d':d}
    tst=render(request,'exam/test.html',context=data)
    return tst
