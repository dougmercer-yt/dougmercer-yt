import time
import numpy as np
import pandas as pd

__all__ = ["get_data"]


def get_data() -> np.ndarray:
    time.sleep(7.5)
    if np.random.random() > 0.5:
        raise RuntimeError("Failed to return data. Try again!")
    
    n_periods = 10
    return pd.Series(
        index=pd.period_range(start='2023-01-01', periods=n_periods, freq='W'),
        data=np.random.normal(loc=50, scale=25, size=(n_periods,)).clip(0, 100),
    )
