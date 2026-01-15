PKW-Django01
กด Ctrl+ฝ เป็นการสร้าง Commend HTML <!-- -->
---------------------------------------------
> สร้าง Database ก่อนด้วย Tool ตัวไหนก็ได้
> mkdir <workfolder>
> cd <workfolder>
> python -m pip install --upgrade pip
> pip install virtualenv
> virtualenv <vm_name>
> .\vm_name\scripts\activate
> pip install -r requirements.txt
> pip list
> django-startproject .
> cd projectname
> python -m manage.py runserver #ทดสอบรันโปรเจกต์
> python manage.py startapp api
---------------------------------------------
ที่ settings.py เพิ่ม
INSTALLED_APPS = [
    'rest_framework',
    'api'
]
---------------------------------------------
to /api/models.py
### Create your models here.
class Member(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    .....

    def __str__(self):
        return self.name

> python manage.py makemigrations
> python manage.py migrate

สร้าง /api/serializers.py
from rest_framework import serializers
from .models import Member

class MemberSerializers(serializers.ModelSerializer):
    model=Member
    fields='__all__'

to /api/views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializers

class MemberViewSet(viewsets.ModelViewSet):
    querySet=Member.objects.all()
    serializer_class=MemberSerializers

to /api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet

router= DefaultRouter()
router.register(r'member',MemberViewSet)
urlpatterns=[
    path('api/',include(router.urls))
]

to /itserv2/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('api.urls')),
]

> python manage.py createsuperuser