from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def start(request):
    return HttpResponse("OK")

def m3t(request):
    return HttpResponse("m3t")

def r2(request):
    return 
