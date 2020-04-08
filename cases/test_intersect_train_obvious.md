## Effect
Overesteemed results.

Size of the effect: if the proportion of intersection between train and test.
"Baseline" exploiting leakerage that only provides matching between test and train has no error on intersection without modeling and generalizing anything.
## Rules to avoid leakage
1) Sanity check in train_test separation
## Quick fix example
```python3
test_samples_from_train = set(train_df[[features]]).intersection(set(test_df[[features]]))
test_new = test_df[~test_df[features].isin(test_samples_from_train)]
```
## Test
[test_intersect_train_obvious.py](/src/leakage_tests/test_intersect_train_obvious.py)
## Incorporation stage
Dataset preparation
## Locate in code 
Train test split and/or duplicate check
## Was met or loosely based on
[kaggle "Arxiv Title Generation" competition YURY KASHNITSKY post](https://www.kaggle.com/code/kashnitsky/arxiv-title-generation-dumb-baseline)
