from django.urls import path

from . import views

app_name ='schoolvoting'

# common views
urlpatterns = [
    path('',views.show_subjects, name="index"),
    path('<int:subject_no>/teachers/',views.teachers, name = "teachers"),
    path('praise/<int:teacher_no>', views.praise_or_criticize, name = 'praise'),
    path('criticize/<int:teacher_no>', views.praise_or_criticize, name='criticize')
]