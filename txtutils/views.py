# I have created this file - Aviral
from django.http import HttpResponse
from django.shortcuts import render



def index(request):

    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default ')
    # Check the Checkbox Value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    is_on=False
    # Chack if which checkbox is on
    if removepunc == 'on':
        is_on=True
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed +=char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps =='on':
        is_on = True
        analyzed=''
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext=analyzed

    if newlineremover =='on':
        is_on = True
        analyzed = ''
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed += char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed

    if extraspaceremover == 'on':
        is_on = True
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] ==' ' and djtext[index+1]==' '):
                analyzed += char
        params = {'purpose': 'Removed Spaces', 'analyzed_text': analyzed}
        djtext=analyzed

    if charcount == 'on':
        is_on = True
        analyzed = "No Of Character is {}".format(len(djtext))
        params = {'purpose': 'Character Counted', 'analyzed_text': analyzed}

    if not(is_on):
        return HttpResponse("ERROR !! please select the Operation !")


    return render(request, 'analyze.html', params)
