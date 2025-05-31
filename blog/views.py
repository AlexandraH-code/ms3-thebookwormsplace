from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
# from django.contrib.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost, Comment, Rating, About
# from .forms import CommentForm, ContactForm


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
    comments = Comment.objects.filter(post=book)
    upvotes = Rating.objects.filter(post=book, value='up').count()
    downvotes = Rating.objects.filter(post=book, value='down').count()

    if request.method == 'POST':
        if 'upvote' in request.POST:
            Rating.objects.get_or_create(user=request.user, post=book, value='up')
        elif 'downvote' in request.POST:
            Rating.objects.get_or_create(user=request.user, post=book, value='down')
        elif 'review_submit' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = book
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


# Login - login form
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})
