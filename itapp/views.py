from django.shortcuts import HttpResponse, render

# Create your views here.


def index(request):
    return HttpResponse('<h1> ยังไม่ได้สร้าง itapp/index.html</h1>')


def home(request):
    return HttpResponse('<h3> ยังไม่ได้สร้าง itapp/home.html</h3>')
