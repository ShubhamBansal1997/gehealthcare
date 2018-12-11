import logging
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
	render,
	HttpResponseRedirect
)
from .models import User
from .forms import LoginForm

logger = logging.getLogger()


def login(request, template_name='pages/login.html'):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/profile/')
	else:
		return render(request, template_name)


def authuser(request, template_name='pages/login.html'):
	'''
	used to login the user
	'''
	authdata = LoginForm(request.POST or None)
	if request.method == 'POST':
		if authdata.is_valid():
			user = User.objects.get(email=authdata.cleaned_data["email"])
			username = user.get_username()
			user = authenticate(
				username=username,
				password=authdata.cleaned_data["password"]
			)
			logger.debug(user, 'authenticated')
			if user is not None:
				logger.debug(user)
				if user.is_active:
					logger.debug(user, 'here')
					auth_login(request, user)
					return HttpResponseRedirect('/profile')
				else:
					messages.error(request, 'User is not active')
			else:
				messages.error(request, 'User Doesnot Exist!')
		else:
			c = {'form': authdata}
			messages.error(request, 'Wrong Credentials!')
			return render(request, template_name, c)
	elif request.user.is_authenticated:
		return HttpResponseRedirect('/profile/')
	else:
		authdata = LoginForm()
		c = {'form': authdata}
		return render(request, template_name, c)


def logout_user(request):
	logout(request)
	request.session.flush()
	return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def profile(request, template_name='pages/profile.html'):
	return render(request, template_name)


