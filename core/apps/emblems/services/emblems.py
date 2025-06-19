from abc import ABC, abstractmethod

from core.apps.emblems.models import Emblem


class BaseService(ABC):
    @abstractmethod
    def get_all_emblems(self):
        ...

    @abstractmethod
    def get_emblem_by_id(self, emblem_id: str):
        ...


class OrmEmblemService(BaseService):
    def get_all_emblems(self):
        return Emblem.objects.all()

    def get_emblem_by_id(self, emblem_id: str):
        emblem = Emblem.objects.filter(id=emblem_id)
        if not emblem.exists():
            return None
        return emblem.first()
