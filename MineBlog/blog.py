from django.shortcuts import render_to_response

from MineBlog.models import Blog


def list_all(request):
    blogs = Blog.objects.all()
    user = request.user
    return render_to_response('list.html', {'blogs': blogs, 'tp_user': user})


def view(request, blog_id):
    blog = Blog.objects.get(id=int(blog_id))
    user = request.user
    return render_to_response('view.html', {'blog': blog, 'tp_user': user})
