from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext

from MineBlog.forms import LoginForm


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form, })
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
                return render(request, 'login.html', {'form': form, 'tp_error_msg': form.errors})
        else:
            return render(request, 'login.html', {'form': form, 'tp_error_msg': form.errors})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/user/login")
