from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RolesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.roles'
    verbose_name = _("Роли")
