from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('karu/', views.karu, name='karu'),
    path('about/', views.about, name='about'),
]
