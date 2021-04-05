from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username, password=None):
        '''Create and save a user with the given email, and
        password.
        '''
        if not username:
            raise ValueError('Users must have an Username!')
        user = self.model(
            username=self.normalize_email(username),
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=self.normalize_email(username),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):

    EXPERIENCE_OPTIONS = [
        ('Beginner', 'Beginner'),
        ('Amateur', 'Amateur'),
        ('Semi-Pro', 'Semi-Pro'),
        ('Professional', 'Professional'),
    ]

    email           = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    username        = models.CharField(verbose_name='Username', max_length=60, unique=True)
    dob             = models.DateField(verbose_name='Date of Birth', null=True, blank=True)
    phone           = models.CharField(max_length=10, null=False, verbose_name="Contact Number")
    about           = models.TextField(verbose_name='About', max_length=500)
    experience      = models.CharField(verbose_name='Experience', max_length=12, choices=EXPERIENCE_OPTIONS)
    date_joined     = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
