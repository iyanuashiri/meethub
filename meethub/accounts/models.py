from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

from meethub.accounts.managers import AccountManager

# Create your models here.


class Account(AbstractBaseUser, PermissionsMixin):
    is_client = models.BooleanField('client status', default=False)

    first_name = models.CharField(_('first name'), max_length=200)
    last_name = models.CharField(_('last name'), max_length=200)
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into the admin site.'),
    )

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_client']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.get_fullname()

    def clean(self):
        super().clean()

    def get_first_name(self):
        """
        Return the first name
        """
        return self.first_name

    def get_fullname(self):
        """
        Return the fullname
        :return: fullname
        """
        fullname = '{} {}'.format(self.last_name, self.first_name)
        return fullname

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
        return True
