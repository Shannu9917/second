from django.shortcuts import render
from django.http import HttpResponse

def app2(request):
    return HttpResponse('This is the app2')

# Create your views here.
