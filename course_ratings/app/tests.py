from django.contrib.auth.models import AnonymousUser, User
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from app.controllers import AuthController

class AuthControllerLoginTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.authController = AuthController()
        self.user = User.objects.create_user(
            username="user", email="user@example.com", password="password"
        )

    def _build_request(self, username, password):
        request = self.factory.post("/login/", {"username": username, "password": password})
        SessionMiddleware(lambda r: None).process_request(request)
        request.session.save()
        request.user = AnonymousUser()
        return request

    def test_login_with_correct_credentials_logs_user_in(self):
        request = self._build_request("user", "password")
        self.authController.login(request)
        self.assertEqual(request.user, self.user)

    def test_login_with_wrong_password_does_not_log_user_in(self):
        request = self._build_request("user", "wrong-password")
        self.authController.login(request)
        self.assertFalse(request.user.is_authenticated)
