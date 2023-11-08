from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def jampandu(request):
    return HttpResponse('Hi jampandu how are you')
def jigelrani(request):
    return HttpResponse('I am fine')