from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class AccountManager(BaseUserManager):
    def create_user(self, account_id, email, name, account_type='ST', password=None):
        if not account_id:
            raise ValueError('Users must have a account id')

        if not email:
            raise ValueError('Users must have an email address')

        account = self.model(
            account_id=account_id,
            account_type=account_type,
            email=email,
            name=name,
        )
        account.set_password(password)
        account.save(using=self._db)

        return account

    def create_superuser(self, account_id, email, name, password):
        account = self.create_user(
            account_id=account_id,
            account_type='AR',
            email=email,
            name=name,
            password=password,
        )
        account.is_admin = True
        account.save(using=self._db)

        return account


class Account(AbstractBaseUser):
    ACCOUNT_TYPE_CHOICES = (
        ('ST', 'Student'),
        ('TA', 'Teaching Assistant'),
        ('PR', 'Professor'),
        ('AR', 'Administrator'),
    )

    idx = models.AutoField(primary_key=True)
    account_id = models.CharField(verbose_name='Account ID',
                                  max_length=30, unique=True)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPE_CHOICES)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'account_id'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.account_id

    def has_perm(self, perm, obj=None):
        return self.is_active

    def has_module_perms(self, app_label):
        return self.is_active

    @property
    def is_staff(self):
        return self.is_admin


class Major(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    college = models.ForeignKey('College', on_delete=models.SET_NULL, null=True)
    accounts = models.ManyToManyField(Account, blank=True)

    def __str__(self):
        return self.name


class College(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
