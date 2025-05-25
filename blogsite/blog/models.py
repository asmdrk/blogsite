from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
    body = models.TextField()
    publish_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True) # date saved automatically on creation
    updated_at = models.DateTimeField(auto_now=True) # date saved automatically on UPDATE

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publish_at']
        indexes = [models.Index(fields=['-publish_at'])]
        
    