# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomUserEditForm
# Decorators
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


@unauthenticated_user
def registerPageView(request):
	form = CustomUserCreationForm()
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f'Поздравляем {username}, Вы успешно зарегистривались!')
			form.save()
			return redirect('login')
	context = {'form': form}
	return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPageView(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else: 
			messages.info(request, 'Неправильно введены имя пользователя или пароль')
	return render(request, 'accounts/login.html', {})



def logoutUser(request):
	logout(request)
	return redirect('home')


@login_required(login_url='login')
def userProfileView(request):
	context = {
		'username': request.user.get_username(),
		'email': request.user.email,
	}
	return render(request, 'accounts/userprofile.html', context)


# @unauthenticated_user
def userProfileEdit(request):
	form = CustomUserEditForm(instance=request.user)
	if request.method == 'POST':		
		form = CustomUserEditForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()	
			return redirect('userprofile')
	context = {'form': form}
	return render(request, 'accounts/edit.html', context)

