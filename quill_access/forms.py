from django.contrib.auth.forms import UserCreationForm
from quill_access import models


class RegisterForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username']
