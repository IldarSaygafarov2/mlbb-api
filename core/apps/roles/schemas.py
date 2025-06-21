import uuid
from typing import Optional

from ninja import Schema


class RoleSchema(Schema):
    id: uuid.UUID
    name: str
    icon: Optional[str] = None
