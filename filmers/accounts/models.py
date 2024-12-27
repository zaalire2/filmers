from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

class AdminUser(User):
    class Meta:
        proxy = False

    def save(self, *args, **kwargs):
        self.is_staff = True
        super().save(*args, **kwargs)

    @property
    def user_type(self):
        return 'admin'

class RegularUser(User):
    class Meta:
        proxy = False

    def save(self, *args, **kwargs):
        self.is_staff = False
        super().save(*args, **kwargs)

    @property
    def user_type(self):
        return 'regular' 