#i have created this file -Anurag
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render (request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    print(djtext)
    removepunc=request.POST.get('removepunc','off')
    charcount=request.POST.get('charcount','off')
    captext=request.POST.get('captext','off')
    spaceremover = request.POST.get('spaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    print(removepunc)
    print(charcount)
    print(spaceremover)
    print(newlineremover)
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if captext == 'on':
        analyzed = djtext.upper()
        params = {'purpose': 'Capitalize Text', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed ExtraSpaces', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djtext = analyzed


    if charcount == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)

    if removepunc=='off' and charcount=='off' and spaceremover=='off' and captext=='off' and newlineremover=='off':
        return render(request, 'noaction.html')


    return render(request, 'analyze.html', params)

