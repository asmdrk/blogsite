from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True) # date saved automatically on creation
    updated_at = models.DateTimeField(auto_now=True) # date saved automatically on UPDATE

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publish_at']
        
    