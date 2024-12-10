from prefect.automations import Automation
from prefect.events.schemas.automations import EventTrigger
from prefect.events.actions import CancelFlowRun

# creating an automation
automation = Automation(
    name="woodchonk",
    trigger=EventTrigger(
        expect={"animal.walked"},
        match={
            "genus": "Marmota",
            "species": "monax",
        },
        posture="Reactive",
        threshold=3,
    ),
    actions=[CancelFlowRun()],
).create()
print(automation)
# name='woodchonk' description='' enabled=True trigger=EventTrigger(type='event', match=ResourceSpecification(__root__={'genus': 'Marmota', 'species': 'monax'}), match_related=ResourceSpecification(__root__={}), after=set(), expect={'animal.walked'}, for_each=set(), posture=Posture.Reactive, threshold=3, within=datetime.timedelta(seconds=10)) actions=[CancelFlowRun(type='cancel-flow-run')] actions_on_trigger=[] actions_on_resolve=[] owner_resource=None id=UUID('d641c552-775c-4dc6-a31e-541cb11137a6')

# reading the automation

automation = Automation.read(id=automation.id)
# or
automation = Automation.read(name="woodchonk")

print(automation)
# name='woodchonk' description='' enabled=True trigger=EventTrigger(type='event', match=ResourceSpecification(__root__={'genus': 'Marmota', 'species': 'monax'}), match_related=ResourceSpecification(__root__={}), after=set(), expect={'animal.walked'}, for_each=set(), posture=Posture.Reactive, threshold=3, within=datetime.timedelta(seconds=10)) actions=[CancelFlowRun(type='cancel-flow-run')] actions_on_trigger=[] actions_on_resolve=[] owner_resource=None id=UUID('d641c552-775c-4dc6-a31e-541cb11137a6')
