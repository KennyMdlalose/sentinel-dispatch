from dataclasses import dataclass, field
from datetime import datetime 

@dataclass
class Guard:
    id: str
    name: str
    x: float
    y: float
    available: bool = True


@dataclass
class Incident: 
    id: str
    event_type: str
    x: float
    y: float
    created_at: datetime
    assigned_guard_id: str | None = None


def distance(ax: float, ay: float, bx: float, by: float) -> float:
    return ((ax - bx) ** 2 + (ay -by) ** 2) ** 0.5


def nearest_available_guard(guards: list[Guard], incident: Incident) -> Guard | None:
    available = [g for g in guards if g.available]
    if not available:
        return None
    return min(available, key=lambda g: distance(g.x, g.y, incident.x, incident.y))



AUTO_DISPATCH_TYPES = {"PANIC", "FIRE"}

def requires_operator_verification(event_type: str) -> bool: 
    return event_type not in AUTO_DISPATCH_TYPES


@dataclass
class DispatchDecision:
    incident_id: str
    action: str # "AUTO_DISPATCH", "AWAIT_OPERATOR", or "NO_GUARD_AVAILABLE"
    guard: Guard | None = None


def decide_dispatch(guards: list[Guard], incident: Incident) -> DispatchDecision:
    if requires_operator_verification(incident.event_type):
        return DispatchDecision(incident_id=incident.id, action="AWAIT_OPERATOR")


    guard = nearest_available_guard(guards, incident)
    if guard is None: 
        return DispatchDecision(incident_id=incident.id, action="NO_GUARD_AVAILABLE")

    return DispatchDecision(incident_id=incident.id, action="AUTO_DISPATCH", guard=guard)