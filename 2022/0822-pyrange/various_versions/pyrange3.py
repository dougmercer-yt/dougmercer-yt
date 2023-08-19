from dataclasses import dataclass
from typing import Any, SupportsIndex


@dataclass(frozen=True, slots=True, init=False)
class pyrange:
    start: int
    stop: int
    step: int

    def __init__(self, /, *args: SupportsIndex):
        # Parse variable number of input arguments
        args = [as_int(x) for x in args]
        if len(args) == 0:
            raise TypeError(f"pyrange expected at least one argument, got {len(args)}")
        elif len(args) > 3:
            raise TypeError(f"pyrange expected at most 3 argument, got {len(args)}")
        elif len(args) == 1:
            start, stop, step = 0, args[0], 1
        elif len(args) == 2:
            start, stop = args
            step = 1
        else:
            start, stop, step = args

        # Guard against 0-length step
        if step == 0:
            raise ValueError("pyrange arg 3 must not be 0")

        # Circumvent the fact that pyrange is frozen
        object.__setattr__(self, "start", start)
        object.__setattr__(self, "stop", stop)
        object.__setattr__(self, "step", step)


def as_int(obj: Any) -> int:
    if hasattr(obj, "__index__"):
        idx = obj.__index__()
        assert isinstance(idx, int)
        return idx
    raise TypeError(f"'{obj.__class__.__name__}' object cannot be interpreted as an integer")
