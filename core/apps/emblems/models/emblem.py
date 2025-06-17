from django.db import models
from django.utils.translation import gettext_lazy as _

from core.apps.base_app.models import BaseModel
from core.apps.emblems.enums import EmblemTypeChoices


class Emblem(BaseModel):
    name = models.CharField(verbose_name=_("Название"), max_length=100, unique=True)
    icon = models.ImageField(
        verbose_name=_("Иконка"), upload_to="emblems/icons/", null=True, blank=True
    )
    emblem_type = models.CharField(
        verbose_name=_("Тип эмблемы"), choices=EmblemTypeChoices.choices, max_length=50
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Эмблема")
        verbose_name_plural = _("Эмблемы")
