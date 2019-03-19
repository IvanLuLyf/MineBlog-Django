from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from MineBlog.forms import LoginForm, RegisterForm


@csrf_protect
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user_login.html', {'form': form, })
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/blog/list")
            else:
                return render(request, 'user_login.html', {'form': form, 'tp_error_msg': form.errors})
        else:
            return render(request, 'user_login.html', {'form': form, 'tp_error_msg': form.errors})


@csrf_protect
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user_register.html', {'form': form, })
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            user = User.objects.create_user(username=username, email=email, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/blog/list")
            else:
                return render(request, 'user_register.html', {'form': form, 'tp_error_msg': form.errors})
        else:
            return render(request, 'user_register.html', {'form': form, 'tp_error_msg': form.errors})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/user/login")
