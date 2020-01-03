from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Emp,Dept

admin.site.register(Dept)
admin.site.register(Emp)