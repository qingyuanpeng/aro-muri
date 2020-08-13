from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    body = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.body
