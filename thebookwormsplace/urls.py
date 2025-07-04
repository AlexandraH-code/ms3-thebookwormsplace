"""
URL configuration for thebookwormsplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from blog import views as blog_views
# from blog import urls as blog_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', blog_views.index, name='index'),
    # path('', include("blog_urls"), name="blog_urls"),  # the app urls are loaded as the main urls
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
