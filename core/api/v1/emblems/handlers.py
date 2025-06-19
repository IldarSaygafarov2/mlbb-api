import typing

from django.http import HttpRequest
from ninja import Router

from core.apps.emblems.services import emblems_service
from .schemas import EmblemSchema

router = Router(tags=['Emblems'])


@router.get('/', response=typing.List[EmblemSchema])
def get_emblems_list(request: HttpRequest):
    return emblems_service.get_all_emblems()


@router.get('/{emblem_id}', response=EmblemSchema)
def get_emblem_by_id(request: HttpRequest, emblem_id: str):
    return emblems_service.get_emblem_by_id(emblem_id=emblem_id)
