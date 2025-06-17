from django.db import models
from django.utils.translation import gettext_lazy as _

from core.apps.base_app.models import BaseModel


class Equipment(BaseModel):
    name = models.CharField(verbose_name=_("Название"), max_length=150, unique=True)
    short_description = models.TextField(
        verbose_name=_("Краткое описание"), null=True, blank=True
    )
    icon = models.ImageField(
        verbose_name="Иконка", upload_to="equipment/icons/", null=True, blank=True
    )
    price = models.IntegerField(verbose_name=_("Цена"))
    equipment_type = models.ManyToManyField(
        "equipment.EquipmentType",
        related_name="equipment_types",
        verbose_name=_("Тип снаряжения"),
    )
    recipe_items = models.ManyToManyField(
        "self",
        verbose_name=_("Рецепт"),
        help_text="Элементы из которых сделан предмет",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        verbose_name = _("Снаряжение")
        verbose_name_plural = _("Снаряжения")
