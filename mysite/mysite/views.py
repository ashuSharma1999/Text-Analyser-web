from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyse(request):
    # get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if(removepunc=="on"):
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyse=""
        for char in djtext:
            if char not in punctuation:
                analyse=analyse+char
        param={'purpose':'Remove Punctuation','analyse_text':analyse}
        djtext=analyse
        # return render(request,'analyse.html',param)
    if(fullcaps=='on'):
        analyse=""
        for char in djtext:
            analyse=analyse+char.upper()
        param={'purpose':'Change to upper case','analyse_text':analyse}
        djtext=analyse
        # return render(request,'analyse.html',param)
    if(newlineremover=='on'):
        analyse=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyse=analyse+char
        param={'purpose':'Line Remover','analyse_text':analyse}
        djtext=analyse
        # return render(request,'analyse.html',param)
    if(extraspaceremover=='on'):
        analyse=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyse=analyse+char 
        param={'purpose':'Extra space remover','analyse_text':analyse}
        djtext=analyse
        # return render(request,'analyse.html',param)
    if(charcount=='on'):
        analyse=len(djtext)
        param={'purpose':'Character count','analyse_text':analyse}
        return render(request,'analyse.html',param)
    if(removepunc !='on' and extraspaceremover !='on' and newlineremover !='on'and charcount !='on'and fullcaps !='on'):
        param={'purpose':'Error ! please select any operation.....Try again !'}
        return render(request,'error.html')
    return render(request,'analyse.html',param)
    
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def feature(request):
    return render(request,'feature.html')