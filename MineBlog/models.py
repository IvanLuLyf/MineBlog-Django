from django.db import models


class Blog(models.Model):
    username = models.TextField()
    nickname = models.TextField()
    title = models.TextField()
    content = models.TextField()
    summary = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
