from django.shortcuts import render
from django.http import HttpResponse


def booklist(request):
    return HttpResponse("You hit the booklist page")

def index(request):
    return HttpResponse("Hello, world. You're at the index page.")


    
