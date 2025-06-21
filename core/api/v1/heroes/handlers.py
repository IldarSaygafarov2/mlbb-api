from django.http import HttpRequest
from ninja import Router

router = Router(tags=["Heroes"])


@router.get("/")
def get_heroes_list(request: HttpRequest):
    return []


@router.get("/specialties/")
def get_hero_specialties(request: HttpRequest):
    """
    Retrieve a list of hero specialties.
    """
    return []
