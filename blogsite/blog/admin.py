from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display= ['title', 'slug', 'author', 'publish_at', 'status']