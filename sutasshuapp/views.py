from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Hello World!')


def add(request):
    return HttpResponse('Upload image here')
