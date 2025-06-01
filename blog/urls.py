from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('books/<int:pk>', views.book_detail, name='book_detail'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
