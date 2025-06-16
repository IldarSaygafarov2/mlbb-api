from core.apps.base_app.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class EquipmentType(BaseModel):
    name = models.CharField(
        verbose_name=_("Название"), unique=True, max_length=100)

    class Meta:
        verbose_name = _("Тип снаряжения")
        verbose_name_plural = _("Типы снаряжений")
