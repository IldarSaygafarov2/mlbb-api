from django.db import models
from django.utils.translation import gettext_lazy as _


class EmblemTypeChoices(models.TextChoices):
    BASE = "BASE", _("Обычная эмблема")
    TANK = "TANK", _("Танк")
    ASSASSIN = "ASSASSIN", _("Убийца")
    MAGE = "MAGE", _("Маг")
    FIGHTER = "FIGHTER", _("Боец")
    SUPPORT = "SUPPORT", _("Поддержка")
    MARKSMAN = "MARKSMAN", _("Стрелок")
