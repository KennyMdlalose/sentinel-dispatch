from enum import Enum
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class EventType(str, Enum):
    PANIC = "PANIC"
    BUGLAR = "BUGLAR"
    TAMPER = "TAMPER"
    FIRE = "FIRE"
    LOW_BATTERY = "RESTORE"

class AlarmEventIn(BaseModel):
    source: str = Field(..., min_length=1, max_length=50)
    panel_code: str = Field(..., min_length=1, max_length=32)
    event_type: EventType
    zone: int | None = Field(None, ge=1)
    occured_at: datetime
    raw: dict | None = None

class AlarmEventAck(BaseModel):
    event_id: UUID
    received_at: datetime
    panel_code: str
    event_type: EventType
    message: str = "Alarm event received"

