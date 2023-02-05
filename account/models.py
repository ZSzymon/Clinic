from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext as _


# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, type, password=None):
        if not email:
            raise ValueError(_('Users must have an email'))
        # if not username:
        #    raise ValueError(_('Users must have an username'))
        if not type:
            raise ValueError(_('Users must have a type'))
        user = self.model(
            email=self.normalize_email(email),
            # username=username,
            type=type,
            is_active=True if type == Account.Types.PATIENT else False,
            is_patient=True if type == Account.Types.PATIENT else False,
        )
        user.set_password(password)
        user.save(using=self._db)
        print('Created User:)')
        return user

    def create_superuser(self, email, type, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            # username=username,
            type=type,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_patient = False

        user.save(using=self._db)
        return user

    def create_staffuser(self, email, type, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            # username=username,
            type=type,
        )
        user.is_admin = False
        user.is_staff = True
        user.is_superuser = False
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DOCTOR = "DOCTOR", "Doctor"
        PATIENT = "PATIENT", "Patient"
        BOOKKEEPER = "BOOKKEEPER", "Bookkeeper"

    email = models.EmailField(_('Email'), max_length=255, unique=True)
    # username = models.CharField(_('Username'), max_length=30, unique=True)
    first_name = models.CharField(_('First name'), null=True, blank=True, max_length=64)
    last_name = models.CharField(_('Last name'), null=True, blank=True, max_length=64)
    adress = models.CharField(_('Adress'), null=True, blank=True, max_length=255)
    money = models.DecimalField(max_digits=6, decimal_places=2, default=1000)

    type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.PATIENT, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('last login'), auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['type', ]

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Note(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=False)
    note = models.TextField(_('Note'), null=True, blank=True)
    is_done = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = 'is completed' if self.is_done else 'is not completed'
        return f'{self.note} {status}'
