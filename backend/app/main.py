from datetime import datetime, timezone
from uuid import uuid4


from fastapi import FastAPI

from .schemas import AlarmEventAck, AlarmEventIn



app = FastAPI(title="Sentinel Dispatch API")


@app.get("/health")
def health():
    return {"status": "working"}

@app.post("/alarm-events", response_model=AlarmEventAck, status_code=202)
def receive_alarm_event(event: AlarmEventIn):
    return AlarmEventAck(
        event_id=uuid4(),
        received_at=datetime.now(timezone.utc),
        panel_code=event_panel,
        event_type=event.event_type,
    )