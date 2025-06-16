import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(
        verbose_name=_("ID"),
        default=uuid.uuid4(), editable=False, primary_key=True
    )

    created_at = models.DateTimeField(
        verbose_name=_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name=_("Дата обновления"), auto_now=True)

    class Meta:
        abstract = True
