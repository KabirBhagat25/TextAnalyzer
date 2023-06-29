# This file is created by use# r
from django.http import HttpResponse
from django.shortcuts import render
#   def index(request):
#     params = {
#              'name': "harry",
#              'place': "Mangolia"
#              }
# return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')
def about(request):
 return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def analyze(request):
    # getting the text from the form in the html
    dj_text = request.GET.get('text', 'default')
    remove_punc = request.GET.get('remove_punc', 'off')
    Upper_Me = request.GET.get('UpperMe', 'off')
    Lower_Me = request.GET.get('LowerMe', 'off')
    Remove_Extra_Spaces = request.GET.get('RemoveSpaces', 'off')
    Remove_New_Line = request.GET.get('RemoveNewLine','off')
    analyze_text = ""

    # print(dj_text)
    #
    # print(Upper_Me)

    # Analyzing the Text
    if (remove_punc == 'on'):
        # analyze_text: str = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in dj_text:
            if(char not in punctuations):
                analyze_text = analyze_text + char
        # params = {
        #             'Purpose': 'Remove Punctuations',
        #             'analyzed_text': analyze_text
        #          }
        dj_text = analyze_text
        analyze_text = ""
        # return render(request, 'analyze.html', params)

    if(Upper_Me == 'on'):
        # analyze_text: str = ""
        for char in dj_text:
             analyze_text = analyze_text + char.upper()
        # params = {
        #             'Purpose': "UPPERCASE",
        #             'analyzed_text': analyze_text
        #          }
        dj_text = analyze_text
        analyze_text = ""
        # return render(request, 'analyze.html', params)

    if (Lower_Me == 'on'):
        # analyze_text: str = ""
        for char in dj_text:
            analyze_text = analyze_text + char.lower()
        # params = {
        #     'Purpose': "LOWERCASE",
        #     'analyzed_text': analyze_text
        # }
        dj_text = analyze_text
        analyze_text = ""
        # return render(request, 'analyze.html', params)

    if(Remove_Extra_Spaces == 'on'):
        # analyze_text: str = ""
        for i, char in enumerate(dj_text):
          if not(dj_text[i] == ' ' and dj_text[i+1] == ' '):
              analyze_text = analyze_text + dj_text[i]
        # params = {'Purpose': 'Remove Extra Spaces',
        #           'analyzed_text': analyze_text
        #          }
        dj_text = analyze_text
        analyze_text = ""
        # return render(request, 'analyze.html',params)

    if (Remove_New_Line == 'on'):
        # analyze_text: str = ""
        for i, char in enumerate(dj_text):
            if not (dj_text[i] == "\n"):
                analyze_text = analyze_text + dj_text[i]

        dj_text = analyze_text
        analyze_text = ""
        # return render(request, 'analyze.html', params)


    if(remove_punc=="off" and Remove_New_Line == "off" and Remove_Extra_Spaces == "off" and Lower_Me == "off" and Upper_Me == "off"):
        return HttpResponse('Error')
    params = {'Purpose': 'Few Opertions',
              'analyzed_text': dj_text
              }
    return render(request, 'analyze.html', params)








