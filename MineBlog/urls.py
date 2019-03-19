"""MineBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from MineBlog import blog, user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.list_all),
    path('user/login', user.login),
    path('user/register', user.register),
    path('user/logout', user.logout),
    path('index', blog.list_all),
    path('blog', blog.list_all),
    path('blog/list', blog.list_all),
    path('blog/create', blog.create),
    url(r'^blog/view/(?P<blog_id>\d+)/$', blog.view),
]
