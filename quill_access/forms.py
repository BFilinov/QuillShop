from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from quill_access import models


class RegisterForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username']


class LoginForm(AuthenticationForm):
    class Meta:
        model = models.User
