from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
# from django.contrib.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost, Comment, Rating, About
from .forms import ContactForm, CommentForm, CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages

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


# Book Detail – show details + handles rating and comments
def book_detail(request, pk):
    book = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(book=book, approved=True).order_by('-created_at')
    upvotes = Rating.objects.filter(book=book, is_upvote=True).count()
    downvotes = Rating.objects.filter(book=book, is_upvote=False).count()

    if request.method == 'POST':
        if 'upvote' in request.POST:
            Rating.objects.get_or_create(user=request.user, book=book, is_upvote=True)
        elif 'downvote' in request.POST:
            Rating.objects.get_or_create(user=request.user, book=book, is_upvote=False)
        elif 'review_submit' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.book = book
                comment.save()
        return redirect('book_detail', pk=book.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/book_detail.html', {
        'book': book,
        'comments': comments,
        'upvotes': upvotes,
        'downvotes': downvotes,
        'form': form
    })


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
            #login(request, user)
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


# Edit Comments - book_details
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


# Delete Comments - book_details
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Your comment was deleted.")
        return redirect('book_detail', pk=comment.book.pk)
    return render(request, 'blog/delete_comment.html', {'comment': comment})
