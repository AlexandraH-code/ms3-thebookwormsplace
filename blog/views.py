from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.db.models import Avg
from .models import BlogPost, Comment, About, StarRating
from .forms import ContactForm, CommentForm, CustomUserCreationForm, CustomAuthenticationForm, UsernameUpdateForm, EmailUpdateForm, PasswordChangeForm, BlogPostForm, AboutForm, StarRatingForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.utils import timezone


# Home
def home(request):
    """
    Render the home page.

    **Template:**
    :template:`blog/home.html`
    """
    return render(request, 'blog/home.html')


# Books – show books
def books(request):
    """
    Display all published books.

    **Context:**
    ``books``: List of published :model:`blog.BlogPost`

    **Template:**
    :template:`blog/books.html`
    """

    books = BlogPost.objects.filter(is_draft=False)
    return render(request, 'blog/books.html', {'books': books})


# Book Detail – show details about book, handle comments and rating
def book_detail(request, slug):
    """
    Display a book's detail page with ratings and comments.

    **Context:**
    ``book``: The :model:`blog.BlogPost` instance
    ``cover_url``: URL of book cover image
    ``comments``: Top-level approved :model:`blog.Comment`
    ``replies``: Approved comment replies
    ``comment_form``: An instance of :form:`blog.CommentForm`
    ``user_rating``: Current user's rating if available
    ``avg_rating``: Average rating value
    ``ratings_count``: Total number of ratings

    **Template:**
    :template:`blog/book_detail.html`
    """
    book = get_object_or_404(BlogPost, slug=slug)
    comments = Comment.objects.filter(book=book, approved=True, parent=None).order_by('-created_at')
    replies = Comment.objects.filter(book=book, approved=True).exclude(parent=None)
    user_rating = None
    avg_rating = None
    ratings_count = 0

    # Try to get image URL, or use placeholder
    try:
        cover_url = book.cover_image.url
    except Exception:
        cover_url = '/static/blog/images/placeholder.jpg'  

    if request.user.is_authenticated:
        user_rating = StarRating.objects.filter(user=request.user, book=book).first()

    avg_data = StarRating.objects.filter(book=book).aggregate(Avg('value'))
    avg_rating = avg_data['value__avg'] or 0
    ratings_count = StarRating.objects.filter(book=book).count()

    comment_form = CommentForm()
    rating_message = None

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                if not request.user.is_authenticated:
                    messages.error(request, "You must be logged in to comment.")
                    return redirect('login')
                
                new_comment = comment_form.save(commit=False)
                new_comment.book = book
                new_comment.user = request.user
                new_comment.approved = False
                parent_id = request.POST.get('parent_id')
                if parent_id:
                    try:
                        parent_comment = Comment.objects.get(id=parent_id)
                        new_comment.parent = parent_comment
                    except Comment.DoesNotExist:
                        pass
                new_comment.save()
                messages.info(request, 'Your comment is awaiting approval.')
                return redirect('book_detail', slug=slug)

        elif 'rate_submit' in request.POST:
            value = request.POST.get('rating')
            if value:
                value = int(value)
                if 1 <= value <= 5:
                    rating, created = StarRating.objects.update_or_create(
                        user=request.user, book=book,
                        defaults={'value': value, 'created_at': timezone.now()}
                    )
                    messages.success(request, "Your rating has been submitted.")
                    return redirect('book_detail', slug=slug)
                else:
                    messages.error(request, "Invalid rating value.")
            else:
                messages.error(request, "Please select a star rating before submitting.")

    context = {
        'book': book,
        'cover_url': cover_url,  
        'comments': comments,
        'replies': replies,
        'comment_form': comment_form,
        'user_rating': user_rating,
        'avg_rating': avg_rating,
        'ratings_count': ratings_count,
    }

    return render(request, 'blog/book_detail.html', context)


# Book detail - edit comment
@login_required
def edit_comment(request, comment_id):
    """
    Edit a user's own comment. Edited comments must be reapproved.

    **Context:**
    ``form``: A prefilled instance of :form:`blog.CommentForm`
    ``comment``: The :model:`blog.Comment` being edited

    **Template:**
    :template:`blog/edit_comment.html`
    """
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            edited_comment = form.save(commit=False)
            edited_comment.approved = False  
            edited_comment.save()
            messages.info(request, 'Your edited comment is awaiting approval.')
            return redirect('book_detail', slug=comment.book.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


# Book detail - delete comment
@login_required
def delete_comment(request, comment_id):
    """
    Delete a user's own comment after confirmation.

    **Context:**
    ``comment``: The :model:`blog.Comment` to confirm deletion

    **Template:**
    :template:`blog/delete_comment.html`
    """
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)

    if request.method == 'POST':
        book_slug = comment.book.slug
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('book_detail', slug=book_slug)

    return render(request, 'blog/delete_comment.html', {'comment': comment})


# About + contactform
def about(request):
    """
    Display the About page content and handle the contact form submission.

    **Context:**
    ``about``: The :model:`blog.About` instance containing the page text.  
    ``form``: An instance of :form:`blog.ContactForm`.

    **Template:**
    :template:`blog/about.html`
    """
    about = About.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent and we will get back to you as soon as possible.")
            return redirect('about')
    else:
        form = ContactForm()
    return render(request, 'blog/about.html', {'about': about, 'form': form})


# Register - registration form
def register(request):
    """
    Display the registration form and create a new user account upon submission.

    **Context:**
    ``form``: An instance of :form:`blog.CustomUserCreationForm`.

    **Template:**
    :template:`blog/register.html`
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your account has been created. Please log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


# Login - login form
def login_view(request):
    """
    Display the login form and authenticate the user upon submission.

    **Context:**
    ``form``: An instance of :form:`blog.CustomAuthenticationForm`.

    **Template:**
    :template:`blog/login.html`
    """
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
    """
    Display a confirmation page for user logout.

    **Template:**
    :template:`blog/logout.html`
    """
    return render(request, 'blog/logout.html')


def logout_view(request):
    """
    Handle the user logout process.

    **Template (redirect):**
    Redirects to :template:`blog/home.html`
    """
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('home')
    return redirect('logout')


"""
User details
"""

# Profile overview
@login_required
def profile_overview(request):
    """
    Display the user's profile overview.

    **Template:**
    :template:`blog/profile_overview.html`
    """
    return render(request, 'blog/profile_overview.html')


# Update username
@login_required
def update_username(request):
    """
    Allow a user to update their username.

    **Context:**
    ``form`` - A form instance of :form:`blog.UsernameUpdateForm`

    **Template:**
    :template:`blog/update_username.html`
    """
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
    """
    Allow a user to update their email address.

    **Context:**
    ``form`` - A form instance of :form:`blog.EmailUpdateForm`

    **Template:**
    :template:`blog/update_email.html`
    """
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
    """
    Allow a user to change their password.

    **Context:**
    ``form`` - A form instance of :form:`blog.PasswordChangeForm`

    **Template:**
    :template:`blog/change_password.html`
    """
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
    """
    Display the admin dashboard with a list of all books.

    **Context:**
    ``books`` - A queryset of all :model:`blog.BlogPost` instances

    **Template:**
    :template:`blog/admin_dashboard.html`
    """
    books = BlogPost.objects.all()
    return render(request, 'blog/admin_dashboard.html', {'books': books})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_add_book(request):
    """
    Admin view to add a new book to the site.

    **Context:**
    ``form`` - A form instance of :form:`blog.BlogPostForm`

    **Template:**
    :template:`blog/admin_add_book.html`
    """
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
    """
    Admin view to edit an existing book.

    **Context:**
    ``form`` - A form instance of :form:`blog.BlogPostForm`

    **Template:**
    :template:`blog/admin_edit_book.html`
    """
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
    """
    Admin view to delete a book.

    **Context:**
    ``book`` - The :model:`blog.BlogPost` instance to be deleted

    **Template:**
    :template:`blog/admin_delete_book.html`
    """
    book = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('admin_dashboard')
    return render(request, 'blog/admin_delete_book.html', {'book': book})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_edit_about(request):
    """
    Admin view to edit the About page content.

    **Context:**
    ``form`` - A form instance of :form:`blog.AboutForm`

    **Template:**
    :template:`blog/admin_edit_about.html`
    """
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
