from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, bunny!")
# Create your views here.
