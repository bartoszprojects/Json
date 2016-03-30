from django.shortcuts import render, HttpResponse
from converter.engine import NumbToWords

def json(request):
    return HttpResponse(NumbToWords(123))
