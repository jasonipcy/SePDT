from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from pdt.models import Project
from pdt.models import Time_Record
from pdt.models import Iteration
from django.contrib.auth.models import User
from datetime import datetime
from pytz import timezone
from django.contrib import auth
from django import template


def hello(request):
    return render(request, 'pdt/hello.html', {'groups': request.user.groups.all()})

def login(request):
	if request.method == 'POST':
		if request.user.is_authenticated(): 
			return render(request, 'pdt/hello.html')

		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)

		if  user is not None and user.is_active:
			auth.login(request, user) #maintain the state of login
			return render(request, 'pdt/hello.html', {'groups': request.user.groups.all()})
		else:
			return render(request, 'pdt/login.html', {'result': "Login Fail! Please try again"})
	else:
		return render(request, 'pdt/login.html')
		
def logout(request):
    auth.logout(request)
    return render(request, 'pdt/hello.html', {'groups': request.user.groups.all()})

def development_page(request):
	# user = User.objects.get(username=request.user)
	# projects = Project.objects.filter(developer_id=user)
	return render(request, 'pdt/development.html', {'projects':Project.objects.filter(developer_id=request.user)})

def log_page(request):
	# user = User.objects.get(username='dev1')
	# luser = LoginUser.objects.get(user=user)
	# user_id = luser.id
	# projects = Project.objects.filter(developer_id=request.user)
	#t_id = Time_Record.objects.values('id').filter(developer_id=user_id)
	# duration = Time_Record.objects.values('duration').filter(developer_id=user_id)
	# time = Time_Record.objects.values('start_time').filter(developer_id=user_id)
	# # phase = 
	# Iteration = Time_Record.objects.values('iteration_id').filter(developer_id=user_id)
	return render(request, 'pdt/log.html', {'projects':Project.objects.filter(developer_id=request.user),'data': Time_Record.objects.filter(developer_id=request.user,activity='dev')})

def set_time(request):
	if request.method == 'POST':
		duration = request.POST.get('duration')
		start_ts = int(request.POST.get('start_ts'))/1000
		end_ts = int(request.POST.get('end_ts'))/1000
		i = Iteration.objects.get(iteration_id=2)
		d = User.objects.get(username=request.user)
		ts = datetime.now(timezone('UTC')).astimezone(timezone('Asia/Hong_Kong'))
		t = Time_Record(iteration_id=i, developer_id=d, activity='dev', start_time=datetime.fromtimestamp(start_ts).strftime('%Y-%m-%d %H:%M:%S'), end_time=datetime.fromtimestamp(end_ts).strftime('%Y-%m-%d %H:%M:%S'), duration=duration)
		t.save()
	return  HttpResponseRedirect('/development/')