import pandas as pd
from typing import Any

def assert_df_group_stratification(train_val_df: pd.DataFrame, 
                                   test_df: pd.DataFrame,
                                   grouping_feature: str) -> None:
    """
    Asserts if group stratification is done correctly for given grouping feature.
    
    Args:
    - grouping_feature (str): The feature used for grouping.
    - train_val_df (pandas.DataFrame): DataFrame containing training and validation data.
    - test_df (pandas.DataFrame): DataFrame containing test data.
    
    Raises:
    - AssertionError: If the group stratification is violated.
    """

    train_val_groups = set(train_val_df[grouping_feature].unique())
    test_groups = set(test_df[grouping_feature].unique())
    group_present_both = train_val_groups.intersection(test_groups)
    assert len(group_present_both)==0, f"group_id's intersection for {group_present_both}"
