import os
from hashlib import sha1, md5
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class UserManger(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Users must have an email address'))
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=25,
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True
    )

    date_joined = models = models.DateTimeField(
        verbose_name=_('Date joined'),
        defailt=timezone.now()
    )
    salt = models.CharField(
        verbose_name=_('Salt'),
        max_length=10,
        blank=True
    )
    objects = UserManger()

    USERNAME_FIELD: 'email'

    class Meta:
        verbose_name=_('user')
        verbose_name_plural=_('users')
        ordering = ('-date_joined',)

    def set_password(self, raw_password):
        salt = md5(os.urandom(128)).hexdigest()[:9]

        hashed = sha1(
            (salt+sha1(
                raw_password.encode('utf8')
            ).hexdigest()).encode('utf8')
        ).hexdigest()

        self.salt = salt
        self.password=hashed

    def check_password(self, raw_password):
        try:
            user = User.objects.get(email=self.email)

            hashed = sha1(
                (user.salt + sha1(
                    (user.salt + sha1(
                        raw_password.encode('utf8')
                    ).hexdigest()).encode('utf8')
                ).hexdigest()).encode('utf8')
            ).hexdigest()

            if user.password == hashed:
                return True
            else:
                return False

        except User.DoesNotExist:
            return False


