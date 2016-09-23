from rest_framework.generics import CreateAPIView
from simple_login.views import (
    RetrieveUpdateDestroyProfileView,
    AccountActivationAPIView,
    LoginAPIView,
    RequestPasswordReset,
    ChangePassword,
)

from app.models import User
from app.serializers import UserSerializer


class Register(CreateAPIView):
    serializer_class = UserSerializer


class Activate(AccountActivationAPIView):
    user_model = User
    serializer_class = UserSerializer


class Login(LoginAPIView):
    user_model = User
    serializer_class = UserSerializer


class Profile(RetrieveUpdateDestroyProfileView):
    user_model = User
    serializer_class = UserSerializer


class ForgotPassword(RequestPasswordReset):
    user_model = User
    serializer_class = UserSerializer


class ChangePasswordView(ChangePassword):
    user_model = User
    serializer_class = UserSerializer
