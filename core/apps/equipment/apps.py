from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EquipmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.equipment'
    verbose_name = _("Снаряжение")
