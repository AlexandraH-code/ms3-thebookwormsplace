from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Create your models here.
class BlogPost(models.Model):
    """
    Stores a single book entry.

    **Fields:**
    - ``title``: The title of the book.
    - ``slug``: URL-friendly identifier, auto-generated from the title.
    - ``author``: The author of the book (as a string).
    - ``cover_image``: Image of the book cover (stored via Cloudinary).
    - ``cover_image_alt``: Alternative text for the cover image.
    - ``description``: Full description of the book.
    - ``created_at``: Timestamp when the book was created.
    - ``updated_on``: Timestamp when the book was last updated.
    - ``is_draft``: Boolean indicating whether the book is a draft.
    - ``excerpt``: Short excerpt from the book.

    **Meta options:**
    - ``ordering``: Newest books appear first.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100)
    cover_image = CloudinaryField('image', default='placeholder')
    cover_image_alt = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.title_changed():
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def title_changed(self):
        if not self.pk:
            return True
        original = BlogPost.objects.get(pk=self.pk)
        return original.title != self.title


class StarRating(models.Model):
    """
    Stores a star rating related to a specific :model:`BlogPost` and :model:`auth.User`.

    **Fields:**
    - ``user``: Reference to the user who submitted the rating.
    - ``book``: Reference to the book that was rated.
    - ``value``: Integer from 1 to 5 representing the rating value.
    - ``created_at``: Timestamp when the rating was submitted.

    **Meta options:**
    - ``unique_together``: Ensures a user can only rate a book once.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='star_ratings')
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f"{self.user} rated {self.book} with {self.value} stars."
    

class Comment(models.Model):
    """
    Stores a comment or reply related to a :model:`BlogPost` and :model:`auth.User`.

    **Fields:**
    - ``user``: The user who wrote the comment.
    - ``book``: The book that the comment is about.
    - ``text``: The body of the comment.
    - ``parent``: Optional reference to another Comment (for replies).
    - ``approved``: Whether the comment has been approved by admin.
    - ``created_at``: Timestamp when the comment was created.

    **Meta options:**
    - ``ordering``: Newest comments appear first.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s comment"


class About(models.Model):
    """
    Stores the content of the About page.

    **Fields:**
    - ``content``: Text field containing the site description.
    """
    content = models.TextField()


class ContactRequest(models.Model):
    """
    Stores messages sent by users through the contact form.

    **Fields:**
    - ``name``: The sender's name.
    - ``email``: The sender's email address.
    - ``message``: The message content.
    - ``created_at``: Timestamp when the message was submitted.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
