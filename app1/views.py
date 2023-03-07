from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_app(request):
    return HttpResponse('This is first app function')

def first_app2(request):
    return HttpResponse('<h1><marquee>This is app2 function</marquee></h1>')