# i have created this file -aaditya
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse('''<h1>Aaditya</h1> <a href="https://www.youtube.com/watch?v=SIyxjRJ8VNY&list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau"> Django code with aaditya </a>''')
def about(request):
    return HttpResponse("hello Aaditya")
def doc_web(request):
    try:
        file = open("text_example.txt", "r+")
        data = file.read()
    except Exception:
        data = '<h2> file is not present in the given directory</h2>'
    return HttpResponse(data)
def ex1(request):
    s = '''<h2> Navigation Bar <br> </h2>
        <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django playlist</a><br>
        <a href="https://www.facebook.com/"> Facebook </a> <br>
        <a href="https://www.flipkart.com/"> Flipkart </a> <br>
        <a href="https://www.hindustantimes.com/"> News </a> <br>
        <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)
def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'capitalize the sentence', 'analyzed_text': analyzed}
        djtext=analyzed

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'char count', 'analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed


    if extraspaceremover == "on":
        analyzed = ""
        for idx, char in enumerate(djtext):
            if djtext[idx] == " " and djtext[idx+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        djtext=analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("please select any option and try again")
    return render(request, 'analyze.html', params)

