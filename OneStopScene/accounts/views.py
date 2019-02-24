from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from accounts.forms import (
	RegistrationForm, 
	EditProfileForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from home.models import Post
from accounts.models import UserProfile
from django.views.generic import UpdateView
from django.forms import inlineformset_factory

def register(request):
	if request.method =='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/home')
	else:
		form = RegistrationForm()
			
		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def view_profile(request, pk = None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
	args = {'user': user}
	return render(request, 'accounts/profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES)
		if form.is_valid():
			return redirect('/home')
			#edit = form.save()
			#edit.user = request.user
			#edit.save()
			#description = form.cleaned_data['description']
			#city = form.cleaned_data['city']
			#website = form.cleaned_data['website']
			#phone = form.cleaned_data['phone']
			#image = form.cleaned_data['image']
			#args = { 'description': description, 
			#	'city': city,
			#	'website': website,
			#	'phone': phone,
			#	'image': image,
			#}
			#return render(request, 'accounts/profile.html', args)
		else:
			return redirect('/home')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts/edit_profile.html', args)
	
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data = request.POST, user = request.user)				
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile')
		else:
			return redirect('/account/change-password')
	else:
		form = PasswordChangeForm(user = request.user)
		args = {'form': form}
		return render(request, 'accounts/change_password.html', args)