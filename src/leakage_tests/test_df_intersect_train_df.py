from typing import Any, List, Set
import pandas as pd

def check_no_df_intersection(train_df: pd.DataFrame, test_df: pd.DataFrame, features: List[str]) -> None:
    """
    Check if there are any common samples between train_df and test_df based on specified features.

    Args:
        train_df (pd.DataFrame): DataFrame containing training data.
        test_df (pd.DataFrame): DataFrame containing test data.
        features (List[str]): List of feature column names to compare.

    Raises:
        AssertionError: If any samples are common between train_df and test_df.
    """
    train_features = train_df[features].apply(tuple, axis=1)
    test_features = test_df[features].apply(tuple, axis=1)
    common_samples = set(train_features).intersection(test_features)
    assert len(common_samples) == 0, "Common samples found between train and test data."