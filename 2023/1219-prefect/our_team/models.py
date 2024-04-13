"""Models, that don't really do anything!"""
import random
import time
from typing import Protocol, Self, runtime_checkable

import numpy as np
import pandas as pd

__all__ = [
    "Model",
    "FastModel",
    "SlowModel",
    "BuggyModel",
    "GoodModel",
    "TerribleModel",
]

SLEEP_MULTIPLIER = 1


@runtime_checkable
class Model(Protocol):
    def fit(self, x: pd.DataFrame) -> Self:
        ...

    def predict(self) -> float:
        ...

    @property
    def name(self) -> str:
        ...


class Named:
    @property
    def name(self) -> str:
        return self.__class__.__name__


class FastModel(Named):
    def fit(self, x: pd.DataFrame) -> Self:
        time.sleep(0.1 * SLEEP_MULTIPLIER)
        return self

    def predict(self) -> float:
        return random.randint(0, 120)


class SlowModel(Named):
    def fit(self, x: pd.DataFrame) -> Self:
        time.sleep(1 * SLEEP_MULTIPLIER)
        return self

    def predict(self) -> float:
        return random.randint(10, 90)


class BuggyModel(Named):
    def fit(self, x: pd.DataFrame) -> Self:
        time.sleep(0.1 * SLEEP_MULTIPLIER)
        if random.random() > 0.5:
            raise RuntimeError("Uh oh...")
        return self

    def predict(self) -> float:
        return random.randint(5, 50)


class GoodModel(Named):
    def fit(self, x: pd.DataFrame) -> Self:
        time.sleep(0.2 * SLEEP_MULTIPLIER)
        return self

    def predict(self) -> float:
        return np.clip(np.random.normal(loc=50, scale=2), 0, 100)


class TerribleModel(Named):
    def fit(self, x: pd.DataFrame) -> Self:
        time.sleep(0.1 * SLEEP_MULTIPLIER)
        return self

    def predict(self) -> float:
        return random.randint(90, 105)
