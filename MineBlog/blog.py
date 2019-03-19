import markdown
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from MineBlog.models import Blog


def list_all(request):
    blog_list = Blog.objects.all()
    user = request.user
    return render_to_response('blog_list.html', {'blog_list': blog_list, 'tp_user': user})


def view(request, blog_id):
    blog = Blog.objects.get(id=int(blog_id))
    blog.content = markdown.markdown(blog.content)
    user = request.user
    return render_to_response('blog_view.html', {'blog': blog, 'tp_user': user})


def create(request):
    if request.method == 'GET':
        user = request.user
        context = {'tp_user': user}
        context.update(csrf(request))
        return render_to_response('blog_create.html', context)
    else:
        blog = Blog()
        blog.username = request.user.username
        blog.nickname = request.user.username
        blog.title = request.POST.get("title", "")
        blog.content = request.POST.get("content", "")
        blog.save()
        return HttpResponseRedirect("/blog/view/" + str(blog.id))
