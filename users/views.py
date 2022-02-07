from django.shortcuts import render,redirect

from django.contrib.auth import login,logout
#premade user form created by django
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#local
from .models import  user


def register(request):
    #this creates a new user using the data from the folder
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #the user is logged
            login(request,user)
            return redirect('tasks:home')
    #this creates a new form to be displayed
    else:
        form=UserCreationForm()
    return render(request,'users/register.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #user is logged
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('tasks:home')
    else:
        form=AuthenticationForm()

    return render(request,'users/login.html',{'form':form})

def logout_view(request):
    if (request.method=='POST'):
        logout(request)
        return redirect('users:login')
