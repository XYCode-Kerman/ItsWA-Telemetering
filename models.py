import datetime
import uuid
from typing import Literal

from pydantic import BaseModel, IPvAnyAddress

EventType = Literal['start', 'close']


class TelmeteringLogIn(BaseModel):
    client_id: str
    event: EventType


class TelmeteringLogDb(TelmeteringLogIn):
    id: uuid.UUID
    time: datetime.datetime
    ip: IPvAnyAddress
