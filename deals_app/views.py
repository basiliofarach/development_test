from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def deals(request):
    return HttpResponse('<h1>Task completed</h1>')
