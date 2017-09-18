from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
    
    