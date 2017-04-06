from django.shortcuts import render
from django.http import request


def home(request):
    cd = {}
    return render(request, 'www/home.html', cd)
