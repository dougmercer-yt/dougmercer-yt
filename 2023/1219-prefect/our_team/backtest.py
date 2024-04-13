import pandas as pd

from .models import Model

__all__ = ["backtest"]


def backtest(model: Model, data: pd.DataFrame) -> pd.Series:
    return pd.Series(
        index=data.index,
        data=[model.fit(data.iloc[:idx]).predict() for idx in range(len(data))],
    )
