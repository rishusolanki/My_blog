from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse ('<h1>My Blog Home Page<h1>')

def about(request):
    return HttpResponse ('<h1>My Blog About Page<h1>')
