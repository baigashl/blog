from django.db import models
from django.utils import timezone
from django.db.models import Model
from django.contrib.auth.models import User


class Post(Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  self.title
