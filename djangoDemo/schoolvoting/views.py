from django.shortcuts import render,redirect
from .models import Subject, Teacher
from django.http import JsonResponse
# Create your views here.

def show_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'schoolvoting/subject.html',{'subjects':subjects})

def teachers(request,subject_no):
    try:

        subject = Subject.objects.get(no=subject_no)
        teachers = subject.teacher_set.all()
        return render(request,'schoolvoting/teachers.html',{
            'subject':subject,
            'teachers':teachers
        })
    except (KeyError,ValueError,Subject.DoesNotExist):
        return redirect('/')

def praise_or_criticize(request,teacher_no):
    try:
        tno=teacher_no
        teacher=Teacher.objects.get(no=tno)
        print(request.path)
        if 'praise' in request.path:
            teacher.good_count+=1
        else:
            teacher.bad_count+=1
        teacher.save()
        data = {'code':200, 'hint':'Operation Successful'}
    except (KeyError,ValueError,Teacher.DoesNotExist):
        data = {'code':404, 'hint':'Operation Failed'}
    return JsonResponse(data)