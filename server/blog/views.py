from django.shortcuts import render

from django.http import HttpResponse


def blog_api(request):
    response = "<h1>Success</h1>"
    return HttpResponse(response)
