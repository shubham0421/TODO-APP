
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.contrib import messages
from .models import *
from .forms import *

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = RegisterForm()
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'tasks/register.html', context)



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'tasks/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')




@login_required(login_url='login')
def home(request):

	form=TaskForm()

	if request.method=='POST':
		form=TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	tasks=Task.objects.all()
	context={'tasks':tasks,'form':form}
	return render(request,'tasks/home.html',context)

@login_required(login_url='login')
def updatetask(request,pk):

	task=Task.objects.get(id=pk)

	form=TaskForm(instance=task)

	if request.method=="POST":
		form=TaskForm(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context={"form":form}
	return render(request,'tasks/update_task.html',context)

@login_required(login_url='login')
def deletetask(request,pk):

	item=Task.objects.get(id=pk)

	if request.method=='POST':
		item.delete()
		return redirect('/')

	context={'item':item}

	return render(request,'tasks/delete.html',context)
