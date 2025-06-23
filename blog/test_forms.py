from django.test import TestCase
from blog.forms import CommentForm, StarRatingForm, CustomUserCreationForm


class CommentFormTest(TestCase):
    def test_comment_form_valid(self):
        form = CommentForm(data={'text': 'Great book!'})
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())


class StarRatingFormTest(TestCase):
    def test_rating_form_valid(self):
        form = StarRatingForm(data={'value': 4})
        self.assertTrue(form.is_valid())

    def test_rating_form_invalid(self):
        form = StarRatingForm(data={'value': 6})
        self.assertFalse(form.is_valid())


class RegisterFormTest(TestCase):
    def test_register_form_valid(self):
        form = CustomUserCreationForm(data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        })
        self.assertTrue(form.is_valid())

    def test_register_form_invalid(self):
        form = CustomUserCreationForm(data={
            'username': 'newuser',
            'email': '',
            'password1': 'pass123',
            'password2': 'differentpass'
        })
        self.assertFalse(form.is_valid())
