from django.shortcuts import render_to_response
import markdown

from MineBlog.models import Blog


def list_all(request):
    blog_list = Blog.objects.all()
    user = request.user
    return render_to_response('list.html', {'blog_list': blog_list, 'tp_user': user})


def view(request, blog_id):
    blog = Blog.objects.get(id=int(blog_id))
    blog.content = markdown.markdown(blog.content)
    user = request.user
    return render_to_response('view.html', {'blog': blog, 'tp_user': user})
