from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#local
from .models import task
from . import forms
# Create your views here.

@login_required(login_url="users:login")
#create a new Task
def newtask(request):
    if request.method=='POST':
        form=forms.CreateTask(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('tasks:home')
    else:
        form=forms.CreateTask()
    return render(request,'tasks/newTask.html',{'form':form})



    #we are using templates on the same folder, inside the folder templates/[APPNAME]
@login_required(login_url="users:login")
def showtasks(request):
    #filter returns an array of objects, check taskDetail for individual queries
    tasksP=task.objects.filter(status='1',author=request.user)
    tasksO=task.objects.filter(status='2',author=request.user)
    tasksF=task.objects.filter(status='3',author=request.user)

    return render(
        request,
        #file in templates/task folder
        'tasks/showTasks.html',
        {
        ##this sends variables to the template, can be used inside as '[NAME]'
            'tasksP':tasksP,
            'tasksO':tasksO,
            'tasksF':tasksF
        }
    )


def taskUpdate(request,slug):
    Task=task.objects.get(slug=slug)
    if Task.status=='1':
        task.objects.get(slug=slug).update(status='2')
    elif Task.status=='2':
        task.objects.get(slug=slug).update(status='3')
    else:
        task.objects.get(slug=slug).delete()
    return redirect('tasks:home')

def taskDetail(request,slug):
    #get obtains an individual object
    Task=task.objects.get(slug=slug)
    return render(request,'tasks/taskDetail.html',{'task':Task})
