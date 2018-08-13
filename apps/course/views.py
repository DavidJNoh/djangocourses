from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages
from .models import Course


def index(request):
    return render(request, "course/index.html", {"stuff":Course.objects.all()})

def delete(request, id):
    return render(request, "course/delete.html", {"stuff":Course.objects.get(id=id)})

def create(request):
    if request.method =="POST":
        errors = Course.objects.validator(request.POST)
        request.session['course_name'] = request.POST['course_name']
        request.session['desc'] = request.POST['desc']
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            course_name = request.POST['course_name']
            desc = request.POST['desc']
            Course.objects.create(course_name=course_name, desc=desc) 
            messages.success(request, "Course added")
            return redirect('/')
    return redirect("/")

def delete_process(request,id):
    b = Course.objects.get(id=id)
    b.delete()
    return redirect("/")

