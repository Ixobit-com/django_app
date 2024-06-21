from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=128)
    first_name = models.CharField(_('first name'), max_length=255, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=255, null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_superuser = models.BooleanField(_('is superuser'), default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('can log into this admin site.'),
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return bool(self.is_staff or self.is_superuser)

    def has_module_perms(self, app_label):
        return bool(self.is_staff or self.is_superuser)
