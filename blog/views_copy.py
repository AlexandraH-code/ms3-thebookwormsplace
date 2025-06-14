from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
# from django.contrib.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Avg
from .models import BlogPost, Comment, About, StarRating
from .forms import ContactForm, CommentForm, CustomUserCreationForm, CustomAuthenticationForm, UsernameUpdateForm, EmailUpdateForm, PasswordChangeForm, BlogPostForm, AboutForm, StarRatingForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Create your views here.
# def index(request):
    # return HttpResponse("Hello, World!")


# Home
def home(request):
    return render(request, 'blog/home.html')


# Books – show books
def books(request):
    books = BlogPost.objects.filter(is_draft=False)
    return render(request, 'blog/books.html', {'books': books})

# Book Detail - Rate book
@login_required(login_url='login')
def rate_book(request, slug):
    book = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST' and request.user.is_authenticated:
        value = request.POST.get('rating')
        if value:
            StarRating.objects.update_or_create(
                user=request.user,
                book=book,
                defaults={'value': int(value)}
            )
            messages.success(request, 'Thank you for rating!')
        else:
            messages.error(request, 'Please select a star rating before submitting.')
    return redirect('book_detail', slug=slug)


# Book Detail – show details about book and handle comments
@require_http_methods(["GET", "POST"])
def book_detail(request, slug):
    book = get_object_or_404(BlogPost, slug=slug)
    comments = Comment.objects.filter(book=book, approved=True, parent__isnull=True).order_by('-created_at')
    replies = Comment.objects.filter(book=book, approved=True, parent__isnull=False)
    reply_dict = {}
    for reply in replies:
        reply_dict.setdefault(reply.parent_id, []).append(reply)

    comment_form = CommentForm()
    user_rating = None
    avg_rating = None
    rating_count = StarRating.objects.filter(book=book).count()

    if request.user.is_authenticated:
        user_rating = StarRating.objects.filter(user=request.user, book=book).first()
        avg_rating = StarRating.objects.filter(book=book).aggregate(avg=Avg('value'))['avg']

        if request.method == 'POST':
            if 'comment_submit' in request.POST:
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    parent_id = request.POST.get('parent_id')
                    parent_comment = Comment.objects.get(id=parent_id) if parent_id else None
                    new_comment = comment_form.save(commit=False)
                    new_comment.book = book
                    new_comment.user = request.user
                    new_comment.parent = parent_comment
                    new_comment.save()
                    messages.info(request, 'Your comment has been submitted and is awaiting approval.')
                    return redirect('book_detail', slug=slug)

    context = {
        'book': book,
        'comments': comments,
        'reply_dict': reply_dict,
        'comment_form': comment_form,
        'user_rating': user_rating,
        'avg_rating': avg_rating,
        'rating_count': rating_count,
    }
    return render(request, 'blog/book_detail.html', context)


# About + contactform
def about(request):
    about = About.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Ev. skicka mail här
            return redirect('about')
    else:
        form = ContactForm()
    return render(request, 'blog/about.html', {'about': about, 'form': form})


# Register - registration form
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Your account has been created. Please log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


# Login - login form
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"You are now logged in as {user.username}.")
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


# Logout
def logout_confirm(request):
    return render(request, 'blog/logout.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('home')
    return redirect('logout')


# Edit Comments - Book Details
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.approved = False  # Eequires new approval from admin
            comment.save()
            messages.info(request, "Your updated comment is awaiting approval.")
            return redirect('book_detail', pk=comment.book.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


# Delete Comments - Book Details
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Your comment was deleted.")
        return redirect('book_detail', pk=comment.book.pk)
    return render(request, 'blog/delete_comment.html', {'comment': comment})

"""
User details
"""

# Profile overview
@login_required
def profile_overview(request):
    return render(request, 'blog/profile_overview.html')

# Update username
@login_required
def update_username(request):
    if request.method == 'POST':
        form = UsernameUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Username updated successfully.")
            return redirect('profile')
    else:
        form = UsernameUpdateForm(instance=request.user)
    return render(request, 'blog/update_username.html', {'form': form})

# Update email
@login_required
def update_email(request):
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Email address updated successfully.")
            return redirect('profile')
    else:
        form = EmailUpdateForm(instance=request.user)
    return render(request, 'blog/update_email.html', {'form': form})

# Change password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            if form.cleaned_data['new_password1'] == form.cleaned_data['old_password']:
                form.add_error('new_password1', "New password cannot be the same as the old one.")
            else:
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Your password was successfully changed.")
                return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'blog/change_password.html', {'form': form})

""" 
Admin view for book management and editing the About page

"""
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    books = BlogPost.objects.all()
    return render(request, 'blog/admin_dashboard.html', {'books': books})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_add_book(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully.")
            return redirect('admin_dashboard')
    else:
        form = BlogPostForm()
    return render(request, 'blog/admin_add_book.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_edit_book(request, pk):
    book = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect('admin_dashboard')
    else:
        form = BlogPostForm(instance=book)
    return render(request, 'blog/admin_edit_book.html', {'form': form})
                            
@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_delete_book(request, pk):
    book = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('admin_dashboard')
    return render(request, 'blog/admin_delete_book.html', {'book': book})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_edit_about(request):
    about, created = About.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, "About page updated successfully.")
            return redirect('admin_dashboard')
    else:
        form = AboutForm(instance=about)
    return render(request, 'blog/admin_edit_about.html', {'form': form})
