from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'itapp/index.html')


def karu(request):
    return render(request, 'itapp/karu.html')


def about(request):
    return render(request, 'itapp/about.html')
