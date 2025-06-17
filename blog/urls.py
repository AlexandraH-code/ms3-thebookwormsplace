from django.urls import path  # import path, similar to project's urls.py
from . import views  # import views.py from the current directory
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    # path('books/<int:pk>', views.book_detail, name='book_detail'),
    path('books/<slug:slug>/', views.book_detail, name='book_detail'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_confirm, name='logout'),
    path('logout/confirmed/', views.logout_view, name='logout_confirmed'),
    # path('comment/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    # path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    # path('profile/edit/', views.profile_edit, name='profile_edit'), 
    path('profile/', views.profile_overview, name='profile'),
    path('profile/username/', views.update_username, name='update_username'),
    path('profile/email/', views.update_email, name='update_email'),
    path('profile/password/', views.change_password, name='change_password'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/add/', views.admin_add_book, name='admin_add_book'),
    path('admin-dashboard/edit/<int:pk>/', views.admin_edit_book, name='admin_edit_book'),
    path('admin-dashboard/delete/<int:pk>/', views.admin_delete_book, name='admin_delete_book'),
    path('admin-dashboard/about/', views.admin_edit_about, name='admin_edit_about'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
