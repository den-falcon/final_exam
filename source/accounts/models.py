from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    username = models.CharField(
        max_length=10,
        verbose_name=_('Имя пользователя'),
        unique=True,
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('Имя'),
    )
    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name=_('Фамилия'),
    )
    phone = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        verbose_name=_('Номер телефона'),
    )
    birth_date = models.DateField(
        null=True,
        blank=False,
        verbose_name=_('Дата рождения'),
    )

    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=False,
        verbose_name=_('Аватар'),
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'
