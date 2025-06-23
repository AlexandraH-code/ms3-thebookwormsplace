from django.contrib import admin
from .models import BlogPost, Comment, About, ContactRequest, StarRating
# uncomment if you want to use Summernote
# from django_summernote.admin import SummernoteModelAdmin 


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, field filters 
    and fields for search.
    """
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'author']


@admin.register(StarRating)
class StarRatingAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, field filters 
    and fields for search.
    """
    list_display = ['user', 'book', 'value', 'created_at']
    list_filter = ['value', 'created_at']
    search_fields = ['user__username', 'book__title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin and field filters.
    """
    list_display = ['user', 'text', 'created_at']
    list_filter = ['created_at']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Lists fields for display.
    """
    list_display = ['id']


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """
    Lists fields for display.
    """
    list_display = ['name', 'email', 'created_at']
