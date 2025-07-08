''''from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")'''
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    temp=loader.get_template('css3.html')
    return HttpResponse(temp.render())
