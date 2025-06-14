from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import BlogPost, Comment, ContactRequest, About, StarRating
# from slugify import slugify
from django.utils.text import slugify


# Form for creating a new user
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# User login form
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


# Form for star rating on the Book details page
class StarRatingForm(forms.Form):
    value = forms.IntegerField(widget=forms.HiddenInput())


# Form for writing a comment on the Book details page
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your thoughts...'}),
        }


# Form for the contact form on the About page
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your message...'}),
        }


# Form for updating username and email
# class UserUpdateForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ['username', 'email']


# Form for updating username
class UsernameUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


# Form for updating email
class EmailUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


# Form for adding and editing books on the Admin page
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'slug',
            'author',
            'cover_image',
            'cover_image_alt',
            'description',
            'excerpt',
            'is_draft',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_image_alt': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'is_draft': forms.CheckboxInput(attrs={'class': 'form-check-input'}),       
        }

    # Styling alla fält med Bootstrap
    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({'class': 'form-control'})

    # Autogenerate slug from title in BlogPostForm
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        slug = cleaned_data.get('slug')

        if title and not slug:
            cleaned_data['slug'] = slugify(title)
        elif title and slugify(title) != slug:
            # Check if it is an existing instance
            if self.instance.pk:
                original_title = BlogPost.objects.get(pk=self.instance.pk).title
                if title != original_title:
                    cleaned_data['slug'] = slugify(title)
        return cleaned_data


# Form for editing text on the About page
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6})
        }
