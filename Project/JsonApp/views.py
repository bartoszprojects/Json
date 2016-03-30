from django.shortcuts import render, HttpResponse
from converter.engine import NumbToWords

def json(request):
    my_number = 432476576532
    o1 = NumbToWords(str(my_number))
    o1.generate_000()
    return HttpResponse(o1.finally_string())
