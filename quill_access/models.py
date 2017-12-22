from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    class Meta:
        app_label = 'quill_access'

    groups = models.ManyToManyField(Group, related_name='group_users')
    user_permissions = models.ManyToManyField(Permission, related_name='permission_users')
