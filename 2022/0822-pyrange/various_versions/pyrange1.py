from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class pyrange:
    start: int
    stop: int
    step: int
