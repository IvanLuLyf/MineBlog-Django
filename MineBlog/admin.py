from django.contrib import admin
from MineBlog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['username', 'nickname', 'title', 'content', 'summary', 'timestamp']


admin.site.register(Blog, BlogAdmin)
