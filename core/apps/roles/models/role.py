from core.apps.base_app.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(BaseModel):
    name = models.CharField(verbose_name=_("Название"),
                            max_length=150, unique=True)
    icon = models.ImageField(verbose_name=_(
        "Иконка"), upload_to='roles/icons/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Роль")
        verbose_name_plural = _("Роли")
