import time
from prefect.events import emit_event

user_id_1, user_id_2 = "123", "456"
for event_name, user_id in [
    ("order.created", user_id_1),
    ("order.created", user_id_2), # other user
    ("order.complete", user_id_1),
]:
    event = emit_event(
        event=event_name,
        resource={"prefect.resource.id": user_id},
    )
    time.sleep(1)
    print(f"{user_id} emitted {event_name}")
