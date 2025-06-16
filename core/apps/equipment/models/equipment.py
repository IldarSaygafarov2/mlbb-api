from core.apps.base_app.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Equipment(BaseModel):
    name = models.CharField(
        verbose_name=_('Название'),
        max_length=150, unique=True
    )
    short_description = models.TextField(verbose_name=_("Краткое описание"))
    icon = models.ImageField(
        verbose_name='Иконка', upload_to='equipment/icons/', null=True, blank=True)
    price = models.IntegerField(verbose_name=_("Цена"))
