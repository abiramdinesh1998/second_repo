from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def string_response(request):
    return HttpResponse('my project sucess')