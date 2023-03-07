from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def second_app(request):
    return HttpResponse('<h1>This is second app function</h1>')

def second_app2(request):
    return HttpResponse('<marquee><h1>This is second app2 function</marquee></h1>')