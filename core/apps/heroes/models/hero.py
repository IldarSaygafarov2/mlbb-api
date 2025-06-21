from django.db import models
from django.utils.translation import gettext_lazy as _

from core.apps.base_app.models import BaseModel


class Hero(BaseModel):
    name = models.CharField(verbose_name=_("Имя героя"), max_length=150, unique=True)
    role = models.ForeignKey(
        "roles.Role",
        verbose_name=_("Роль"),
        on_delete=models.CASCADE,
        related_name="heroes",
    )
