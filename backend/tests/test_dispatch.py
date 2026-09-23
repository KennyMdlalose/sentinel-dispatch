from datetime import datetime

from app.dispatch import Guard, Incident, decide_dispatch

def make_incident(event_type: str, x: float = 1, y: float = 1) -> Incident:
    return Incident(id="i1", event_type=event_type, x=x, y=y, created_at=datetime.now())



def test_panic_auto_dispatches_to_nearest_guard():
    guards = [
        Guard(id="g1", name="Sipho", x=1, y=2),
        Guard(id="g2", name="Thandi", x=8, y=8),
    ]
    incident = make_incident("PANIC")

    decision = decide_dispatch(guards, incident)

    assert decision.action == "AUTO_DISPATCH"
    assert decision.guard.name == "Sipho"



def test_buglar_waits_for_operator():
    guards = [Guard(id="g1", name="Sipho", x=1, y=2)]
    incident = make_incident("BUGLAR")

    decision = decide_dispatch(guards, incident)

    assert decision.action == "AWAIT_OPERATOR"
    assert decision.guard is None


def test_panic_with_no_guards_available():
    guards = [Guard(id="g1", name="Sipho", x=1, y=2, available=False)]
    incident = make_incident("PANIC")

    decision = decide_dispatch(guards, incident)

    assert decision.action == "NO_GUARD_AVAILABLE"


def test_fire_also_auto_dispatches():
    guards = [
        Guard(id="g1", name="Sipho", x=1, y=2),
        Guard(id="g2", name="Thandi", x=8, y=8),
    ]
    incident = make_incident("PANIC")

    decision = decide_dispatch(guards, incident)

    assert decision.action == "AUTO_DISPATCH"
    assert decision.guard.name == "Sipho"
