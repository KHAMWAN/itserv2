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
    'rest_framwork',
    'api'
]
---------------------------------------------
to /api/models.py
### Create your models here.
class User(models.model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    .....

    def __str__(self):
        return self.name