from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
from webapp.choices import AdvertisementStatusChoices


class Advertisement(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        related_name='advertisements',
        on_delete=models.CASCADE,
        verbose_name=_('Автор'),
    )
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name=_('Заголовок'),
    )
    description = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name=_('Описание'),
    )
    category = models.ForeignKey(
        'webapp.Category',
        null=False,
        blank=False,
        related_name='ads',
        on_delete=models.PROTECT,
        verbose_name=_('Категория'),
    )
    image = models.ImageField(
        upload_to='ad_images/',
        null=False, blank=False,
        verbose_name=_('Фото объявления'),
    )
    price = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_('Цена'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Дата редактирования'),
    )
    publicated_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('Дата публикации'),
    )
    status = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        default='on_moderation',
        choices=AdvertisementStatusChoices.choices,
        verbose_name=_('Статус')
    )
    is_deleted = models.BooleanField(default=False, verbose_name=_('Удалено'))

    class Meta:
        db_table = 'advertisements'
        verbose_name = _('Объявление')
        verbose_name_plural = _('Объявления')

    def __str__(self) -> str:
        return f'{self._meta.verbose_name} №{self.id}'


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name=_('Название'),
    )
    description = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name=_('Описание'),
    )

    class Meta:
        db_table = 'categories'
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self) -> str:
        return f'{self.name}'
