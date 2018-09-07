from django.db import models


class Blog(models.Model):
    username = models.TextField()
    nickname = models.TextField()
    title = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField()
