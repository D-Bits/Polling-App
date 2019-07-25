from django.shortcuts import render
from django.http import HttpResponse

# first, dummy view
def index(request):

    return HttpResponse('Hello from Polls Index.')
    
