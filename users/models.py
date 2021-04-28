from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth import get_user_model


"""
To construct a custom user model we need to inherit from BaseUserManager
and AbstractBaseUser
"""
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
USER_REGEX = '^[a-zA-Z0-9.+-]*$'


class AppUserManager(BaseUserManager):
    """
    The model Manager class
    """
    def create_user(self, username, first_name, last_name, email, password=None):
        """
        This function handle the creation of new user into the app,
        and the handle the authentication.
        """
        if not email:
            raise ValueError('Email is required')
        user = self.model(
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            email=self.normalize_email(email),
                        )
        user.set_password(password)
        user.is_user = True
        user.is_demo = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password=None):
        """
        This function handle the creation of superuser, which it will be use have access
        to django admin interface.
        """
        user = self.create_user(
                username,
                first_name,
                last_name,
                email,
                password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_demo = False
        user.is_user = False
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """This class handle the main authenthication, the field that is required
    is outline in this class."""
    username = models.CharField(max_length=255,
                validators=[
                RegexValidator(regex=USER_REGEX,
                message='Username must be alphanumeric',
                code='invalid_username')
                ],
                unique=True
                )
    first_name = models.CharField(max_length=50, unique=False,
            verbose_name='First Name'
            )
    last_name = models.CharField(max_length=50, unique=False,
            verbose_name='Last Name')
    email = models.EmailField(max_length=255, unique=False,
            verbose_name='Email Address')

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_demo = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    objects = AppUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def __str__(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name


    def get_full_name(self):
        """
            Return first name and Last name in the User Dashboard
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    """"The class enable users to update their profile data"""
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
