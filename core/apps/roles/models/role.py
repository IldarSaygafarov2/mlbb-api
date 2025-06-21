from core.apps.base_app.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.apps.roles.schemas import RoleSchema


class Role(BaseModel):
    name = models.CharField(verbose_name=_("Название"), max_length=150, unique=True)
    icon = models.ImageField(
        verbose_name=_("Иконка"), upload_to="roles/icons/", null=True, blank=True
    )

    def to_entity(self) -> RoleSchema:
        """
        Convert the Role instance to a RoleSchema entity.

        Returns:
            RoleSchema: The schema representation of the role.
        """
        return RoleSchema(
            id=self.id,
            name=self.name,
            icon=self.icon.url if self.icon else None,
        )

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        verbose_name = _("Роль")
        verbose_name_plural = _("Роли")
