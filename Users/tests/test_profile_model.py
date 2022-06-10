from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from Users.models import Profile


class ProfileModelTests(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testemail@example.com',
            password='secret')

    def test_profile_user(self):
        profile = Profile.objects.create(user=self.user)

