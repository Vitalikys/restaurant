import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

ROLE_CHOICES = (
    (0, 'employee'),
    (1, 'restaurant'),
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        """
        Creates and saves a RestarauntUser with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None):
        """
        Creates and saves a superuser with the given email, password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
        )
        user.is_admin = True
        user.role = 1
        user.save(using=self._db)
        return user


class RestaurantUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=20, default=None, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(editable=False, auto_now=datetime.datetime.now())
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    id = models.AutoField(primary_key=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)  # Restaurant, STAFF, superuser

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return f' {self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin
