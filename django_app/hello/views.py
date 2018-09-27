from django.shortcuts import render
from django.http import HttpResponse

def index(request, age, nickname):
    result = 'your account: ' + nickname + '" (' + str(age) + ').'
    return HttpResponse(result)
    