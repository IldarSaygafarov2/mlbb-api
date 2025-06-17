from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EmblemsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.emblems"
    verbose_name = _("Эмблемы")
