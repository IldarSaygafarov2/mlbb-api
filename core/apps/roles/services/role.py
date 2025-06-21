from abc import ABC, abstractmethod

from core.apps.roles.models import Role
from core.apps.roles.schemas import RoleSchema


class BaseRoleService(ABC):
    @abstractmethod
    def get_all_roles(self) -> list[RoleSchema]:
        """Retrieve all roles."""
        pass

    @abstractmethod
    def get_role_by_id(self, role_id: str) -> dict:
        """Retrieve a role by its ID."""
        pass


class OrmRoleService(BaseRoleService):
    def get_all_roles(self) -> list[RoleSchema]:
        """Retrieve all roles from the database."""
        roles = Role.objects.all()
        return [role.to_entity() for role in roles]

    def get_role_by_id(self, role_id: str) -> dict:
        """Retrieve a role by its ID from the database."""
        return {}
