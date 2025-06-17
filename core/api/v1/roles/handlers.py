from django.http import HttpRequest
from ninja import Router


router = Router(
    tags=['Roles']
)


@router.get('/')
def get_roles_list(request: HttpRequest):
    return []
