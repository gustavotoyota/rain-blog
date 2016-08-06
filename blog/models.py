from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey(Post, blank=True, null=True)
    author = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.author