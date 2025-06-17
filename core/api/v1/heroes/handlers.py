from ninja import Router
from django.http import HttpRequest

router = Router(tags=['Heroes'])


@router.get('/')
def get_heroes_list(request: HttpRequest):
    return []
