# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View #Possibily unneccesary


def index(request):
	return render(request, 'homepage/index.html')

'''class UserFormView(View):
	form_class = UserForm
	template_name = 'homepage/registration_form.html'

	# Display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# Process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			# cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password) # How to change a password
			user.save()

			# returns User objects if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('homepage:index')
					
		return render(request, self.template_name, {'form': form})'''

