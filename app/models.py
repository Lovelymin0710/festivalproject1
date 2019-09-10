from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    user = models.CharField(max_length=10)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()