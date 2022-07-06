# I have created this file - Vj
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyazed_text': analyzed}
        djtext = analyzed
    
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'purpose':'Changed to Upper', 'analyazed_text': analyzed}
        djtext = analyzed
    
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose':'Removed NewLines', 'analyazed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose':'Removed Extra spaces', 'analyazed_text': analyzed}

    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please select any operation and try again")
    
    return render(request,'analyze.html', params)
