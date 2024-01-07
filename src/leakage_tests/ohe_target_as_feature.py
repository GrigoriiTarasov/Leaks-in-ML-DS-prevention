import numpy as np
import pandas as pd
from typing import Any

def check_target_in_ohe_col(X_train: pd.DataFrame, y_train: Any) -> None:
    """
    Check if any column in X_train is equal to 1 - target.

    Args:
        X_train (pd.DataFrame): DataFrame containing training features.
        y_train: Target variable.

    Raises:
        AssertionError: If any column in X_train is equal to 1 - target.
    """
    for col in X_train.columns:
        assert not np.allclose(X_train[col].values, 1 - y_train), f'"{col}" column is equal to target minus one'
