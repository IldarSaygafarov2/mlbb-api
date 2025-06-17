from django.db import models
from core.apps.base_app.models import BaseModel
from django.utils.translation import gettext_lazy as _


class EquipmentStata(BaseModel):
    name = models.CharField(verbose_name=_('Название'), max_length=100)
    value = models.IntegerField(verbose_name=_("Значение"))
    equipment = models.ForeignKey(
        'equipment.Equipment', on_delete=models.CASCADE, verbose_name=_("Снаряжение"),
        related_name='equipment_stata'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Статистика снаряжения')
        verbose_name_plural = _("Статистика снаряжений")
