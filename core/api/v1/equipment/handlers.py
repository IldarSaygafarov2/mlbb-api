from django.http import HttpRequest
from ninja import Router

router = Router(
    tags=['Equipment']
)


@router.get('/')
def get_equipment_list(request: HttpRequest):
    return []
