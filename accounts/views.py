from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User

def login_view(request):
	next = request.GET.get('next')
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
				return redirect(next)
		return redirect("/")
	return render(request, "Users/loginPage.html", {"form":form, "title":title})

@user_passes_test(lambda user: user.is_superuser)
def register_view(request):
	title = "Create User"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		return redirect("/")
	return render(request, "Users/loginPage.html", {"form":form, "title":title})

def logout_view(request):
	logout(request)
	return redirect("/")


@user_passes_test(lambda user: user.is_superuser)
def list_users(request):
    users_list = User.objects.all()
    return render(request, 'Users/list_users.html', {'entries' : users_list})

# allows user to delete selected model
@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    # grab and delete object
    entry = get_object_or_404(User, pk=pk)
    entry.delete()
    # return HttpResponse('deleted')
    # proceed to reservatio home
    users_list = User.objects.all()
    return render(request, 'Users/list_users.html', {'entries' : users_list})