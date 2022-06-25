from django.db.models import TextChoices
from django.utils.translation import gettext as _


class AdvertisementStatusChoices(TextChoices):
    ON_MODERATION = 'on_moderation', _('На модерации')
    PUBLISHED = 'published', _('Опубликовано')
    REJECTED = 'rejected', _('Отклонено')
