from django.shortcuts import render, redirect
from .models import Student, Grades

def home(request):

    return render(request, 'main_website/home.html', {})

def registered_courses(request):
    grades = Grades.objects.filter(student_id='20210031')

    context = {
        'grades' : Grades.objects.filter
    }
    return render(request, 'main_website/registered_courses.html', context)