import time
from typing import Callable

import pandas as pd

__all__ = ["Metric", "metric"]

Metric = Callable[[pd.DataFrame, pd.DataFrame], float]


def metric(truth: pd.DataFrame, pred: pd.DataFrame) -> float:
    """A basic implementation of root-mean squared error"""
    time.sleep(5)
    return (((truth - pred) ** 2).sum() / len(truth)) ** 0.5
