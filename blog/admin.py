from django.contrib import admin
from .models import BlogPost, Comment, Rating, About, ContactRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'is_draft')
    search_fields = ['title']
    list_filter = ('is_draft',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


# Register your models here.
# admin.site.register(BlogPost)
admin.site.register(About)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(ContactRequest)