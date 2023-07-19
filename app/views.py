from django.shortcuts import render

## Create your views here.

def display_filter(request):
    d = {'data':'Hai Tushar Kumar HOw aRe yoU aR'}
    return render(request, 'user_defined_filter.html',d)
