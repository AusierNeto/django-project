from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1 style={\'text-color\':\'green\'}>Hello World!</h1>')
