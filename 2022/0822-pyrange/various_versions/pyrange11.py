from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Iterator, SupportsIndex


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

    def __iter__(self) -> Iterator[int]:
        value = self.start
        if self.step > 0:
            while value < self.stop:
                yield value
                value += self.step
        else:
            while value > self.stop:
                yield value
                value += self.step

    def __contains__(self, query: Any) -> bool:
        if not isinstance(query, int):
            return False
        if self.step > 0 and not (self.start <= query < self.stop):
            return False
        elif self.step < 0 and not (self.start >= query > self.stop):
            return False
        return (query - self.start) % self.step == 0

    def __len__(self) -> int:
        return max(1 + (self.stop - self.start - sign(self.step)) // self.step, 0)

    def count(self, key: Any) -> int:
        return int(key in self)

    def index(self, value: int) -> int:  # type: ignore [override]
        """Return index of value.

        Raise ValueError if the value is not present.
        """
        if value not in self:
            raise ValueError(f"{value} is not in range")

        return (value - self.start) // self.step

    def __hash__(self) -> int:
        if not len(self):
            return hash((len(self), None, None))
        if len(self) == 1:
            return hash((len(self), self.start, None))
        return hash((len(self), self.start, self.step))

    def __repr__(self) -> str:
        if self.step == 1:
            return f"{self.__class__.__name__}({self.start}, {self.stop})"
        else:
            return f"{self.__class__.__name__}({self.start}, {self.stop}, {self.step})"

    def __getitem__(self, key: SupportsIndex | slice) -> int | pyrange:
        if isinstance(key, slice):
            # Call a helper function to handle the ugly details of simultaneously
            # replacing None-values and clamping the slice to the extents of the range.
            start_slice, stop_slice, step_slice = key.indices(len(self))
            return pyrange(
                self.start + self.step * start_slice,
                self.start + self.step * stop_slice,
                self.step * step_slice,
            )

        key = as_int(key)
        if key < 0:
            key += len(self)

        if not (0 <= key < len(self)):
            raise IndexError("Index out of range.")

        return self.start + key * self.step

    def __reversed__(self) -> Iterator[int]:
        return iter(self[::-1])


def as_int(obj: Any) -> int:
    if hasattr(obj, "__index__"):
        idx = obj.__index__()
        assert isinstance(idx, int)
        return idx
    raise TypeError(f"'{obj.__class__.__name__}' object cannot be interpreted as an integer")


def sign(x: float) -> int:
    return int(math.copysign(1, x))
