# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View #Possibily unneccesary
from django.contrib.auth.forms import UserCreationForm


def index(request):
	return render(request, 'homepage/index.html')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'homepage/signup.html', {'form': form})

def login(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'homepage/login.html', {'form': form})


def logout(request):
	return render(request, 'homepage/index.html')