from django.contrib import admin
from .models import Teacher,Subject
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no','name','create_date','is_hot')
    ordering = ('no',)

class TeachAdmin(admin.ModelAdmin):
    list_display = ('no','name','detail','good_count','bad_count','subject')
    ordering = ('subject','no')

admin.site.register(Subject,SubjectAdmin)
admin.site.register(Teacher,TeachAdmin)