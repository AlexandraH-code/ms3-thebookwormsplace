from django.contrib import admin
from .models import BlogPost, Comment, About, ContactRequest, StarRating
# uncomment if you want to use Summernote
# from django_summernote.admin import SummernoteModelAdmin 


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'author']

@admin.register(StarRating)
class StarRatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'value', 'created_at']
    list_filter = ['value', 'created_at']
    search_fields = ['user__username', 'book__title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'created_at']
    list_filter = ['created_at']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']

"""
# If you want to use Summernote, delete the " before and after class PostAdmin
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'is_draft')
    search_fields = ['title']
    list_filter = ('is_draft',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)
"""
# Register your models here.
# admin.site.register(BlogPost)
# admin.site.register(About)
# admin.site.register(Rating)
# admin.site.register(Comment)
# admin.site.register(ContactRequest)
