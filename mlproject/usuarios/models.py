from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        new_user = User(
            email=self.normalize_email(email),
        )

        new_user.is_staff = False
        new_user.is_active = True

        if password:
            new_user.set_password(password)

        new_user.save()

        return new_user
    
    def create_superuser(self, email, password):
        new_user = self.create_user(email, password)

        new_user.is_active = True
        new_user.is_staff = True
        new_user.is_superuser = True

        new_user.set_password(password)

        new_user.save()

        return new_user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name = 'User email',
        max_length = 194,
        unique=True
    )

    is_active = models.BooleanField(
        verbose_name='Activer user',
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name='User is Staff Member',
        default=False
    )

    is_superuser = models.BooleanField(
        verbose_name='User is superuser',
        default=False,
    )

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'
        db_table='user'

    def __str__(self):
        return self.email