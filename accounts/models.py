from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


"""https://www.youtube.com/watch?v=HshbjK1vDtY&t=2512s"""


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not first_name:
            raise ValueError('Nie podałeś imienia')
        if not last_name:
            raise ValueError('Nie podałeś nazwiska')
        if not email:
            raise ValueError('Nie podałeś adresu email')
        if not password:
            raise ValueError('Nie podałeś hasła')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, first_name, last_name, email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        if not first_name:
            raise ValueError('Nie podałeś imienia')
        if not last_name:
            raise ValueError('Nie podałeś nazwiska')
        if not email:
            raise ValueError('Nie podałeś adresu email')
        if not password:
            raise ValueError('Nie podałeś hasła')

        user = self.create_user(email, first_name, last_name, password=password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        if not first_name:
            raise ValueError('Nie podałeś imienia')
        if not last_name:
            raise ValueError('Nie podałeś nazwiska')
        if not email:
            raise ValueError('Nie podałeś adresu email')
        if not password:
            raise ValueError('Nie podałeś hasła')

        user = self.create_user(email, first_name, last_name, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]  # Email &amp; Password are required by default.

    objects = UserManager()

    class Meta:
        verbose_name = 'Użytkownik'
        verbose_name_plural = 'Użytkownicy'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff


    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin
