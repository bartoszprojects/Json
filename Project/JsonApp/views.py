from django.shortcuts import render, render_to_response, HttpResponse
from converter.engine import NumbToWords
from django.http import JsonResponse


def json(request):
    numb = request.GET.get('number')
    label = NumbToWords(str(numb))
    label.generate_000()

    return JsonResponse({numb: label.finally_string()})






