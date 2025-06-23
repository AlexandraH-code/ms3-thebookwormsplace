from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import BlogPost


class BookViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.book = BlogPost.objects.create(title='Book One', slug='book-one', is_draft=False)

    def test_books_view_status_code(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    def test_book_detail_view_status_code(self):
        response = self.client.get(reverse('book_detail', args=['book-one']))
        self.assertEqual(response.status_code, 200)

    def test_comment_requires_login(self):
        response = self.client.post(reverse('book_detail', args=['book-one']), data={
            'text': 'Nice', 'comment_submit': True
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_authenticated_comment(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.post(reverse('book_detail', args=['book-one']), data={
            'text': 'Nice', 'comment_submit': True
        })
        self.assertEqual(response.status_code, 302)


class AuthViewsTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser2', password='pass123')

    def test_register_view_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_register_view_post(self):
        response = self.client.post(self.register_url, data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Testpass123!',
            'password2': 'Testpass123!'
        })
        self.assertEqual(response.status_code, 302)

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)


class ProfileViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='profileuser', password='oldpassword')
        self.client.login(username='profileuser', password='oldpassword')

    def test_change_password(self):
        response = self.client.post(reverse('change_password'), data={
            'old_password': 'oldpassword',
            'new_password1': 'Newpass123!',
            'new_password2': 'Newpass123!'
        })
        self.assertEqual(response.status_code, 302)


class AdminViewsTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')
        self.client.login(username='admin', password='adminpass')

    def test_admin_add_book(self):
        response = self.client.post(reverse('admin_add_book'), data={
            'title': 'Admin Book',
            'slug': 'admin-book',
            'author': 'Admin',
            'cover_image_alt': 'Alt text',
            'description': 'Book description',
            'is_draft': False,
        })
        self.assertEqual(response.status_code, 302)
