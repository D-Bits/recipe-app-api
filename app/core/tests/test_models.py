from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):

        """Test creating a new user with an email and password"""
        email = "test@gmail.com"
        password = "crappypass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):

        """Test the email for a new user is normalized"""
        email = "test@GMAIL.com"
        user = get_user_model().objects.create_user(email, "blahblah")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):

        """Test that creating user w/o email raises error"""
        with self.assertRaises(ValueError):

            get_user_model().objects.create_user(None, "testing123")

    # Test creating new superusers
    def test_new_superuser(self):
        
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)