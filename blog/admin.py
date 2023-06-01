from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'created_at', 'created_by', 'published_at', 'published_by']
    list_filter = ['is_premium']
    search_fields = ['title', 'body']
