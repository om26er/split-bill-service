from django.conf.urls import url

from app.views import (
    Register,
    Activate,
    Login,
    Profile,
    ForgotPassword,
    ChangePasswordView,
)

urlpatterns = [
    url(r'^api/user/register$', Register.as_view()),
    url(r'^api/user/activate$', Activate.as_view()),
    url(r'^api/user/login$', Login.as_view()),
    url(r'^api/user/me$', Profile.as_view()),
    url(r'^api/user/forgot-password$', ForgotPassword.as_view()),
    url(r'^api/user/change-password', ChangePasswordView.as_view()),
]
