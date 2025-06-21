from core.apps.base_app.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class HeroSpecialty(BaseModel):
    name = models.CharField(
        verbose_name=_("Название специализации"), max_length=150, unique=True
    )
    description = models.TextField(verbose_name=_("Описание специализации"), blank=True)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        verbose_name = _("Специализация героя")
        verbose_name_plural = _("Специализации героев")
