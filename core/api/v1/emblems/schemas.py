import typing as tp
import uuid

from ninja import Schema


class EmblemSchema(Schema):
    id: uuid.UUID
    icon: tp.Optional[str]
    emblem_type: str
