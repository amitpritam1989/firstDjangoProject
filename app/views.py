from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def amit(request):
    return HttpResponse('<h1><marquee>My name is Barry Allen and i am the fastest man alive</marquee></h1>')
