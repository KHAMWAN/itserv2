from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('karu/', views.karu, name='karu'),
    path('repair/', views.repair, name='repair'),
    path('report/', views.report, name='report'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
