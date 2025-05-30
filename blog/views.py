from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
# from django.contrib.forms import UserCreationForm, AuthenticationForm
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