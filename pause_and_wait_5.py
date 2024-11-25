from typing import Literal

import pydantic
from prefect import flow
from prefect.flow_runs import pause_flow_run
from prefect.logging import get_run_logger
from prefect.input import RunInput

# This code causes the flow run to continually pause until the user enters a valid age.


class ShirtOrder(RunInput):
    size: Literal["small", "medium", "large", "xlarge"]
    color: Literal["red", "green", "black"]

    @pydantic.model_validator(mode="after")
    def validate_age(self):
        if self.color == "green" and self.size == "small":
            raise ValueError(
                "Green is only in-stock for medium, large, and XL sizes."
            )

        return self


@flow
def get_shirt_order():
    logger = get_run_logger()
    shirt_order = None

    while shirt_order is None:
        try:
            shirt_order = pause_flow_run(wait_for_input=ShirtOrder)
        except pydantic.ValidationError as exc:
            logger.error(f"Invalid size and color combination: {exc}")

    logger.info(
        f"Shirt order: {shirt_order.size}, {shirt_order.color}"
    )

