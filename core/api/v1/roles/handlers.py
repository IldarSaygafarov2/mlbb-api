from django.http import HttpRequest
from ninja import Router

from core.apps.roles.schemas import RoleSchema
from core.apps.roles.services import orm_role_service

router = Router(
    tags=["Roles"],
)


@router.get("/", response=list[RoleSchema])
def get_roles_list(request: HttpRequest):
    return orm_role_service.get_all_roles()
