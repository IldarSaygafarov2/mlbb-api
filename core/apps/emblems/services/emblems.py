import typing
from abc import ABC, abstractmethod

from core.apps.emblems.models import Emblem
from django.db.models import QuerySet


class BaseService(ABC):
    @abstractmethod
    def get_all_emblems(self) -> QuerySet[Emblem]: ...

    @abstractmethod
    def get_emblem_by_id(self, emblem_id: str) -> typing.Optional[Emblem]: ...


class OrmEmblemService(BaseService):
    def get_all_emblems(self) -> QuerySet[Emblem]:
        return Emblem.objects.all()

    def get_emblem_by_id(self, emblem_id: str) -> typing.Optional[Emblem]:
        emblem = Emblem.objects.filter(id=emblem_id)
        if not emblem.exists():
            return None
        return emblem.first()
