from django.contrib import admin
from .models import BlogPost, Comment, Rating, About, ContactReguest


# Register your models here.
admin.site.register(BlogPost)
admin.site.register(About)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(ContactReguest)