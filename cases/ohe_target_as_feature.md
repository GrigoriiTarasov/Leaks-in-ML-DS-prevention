## Effect
 Up to 100% for model equals 1-ohe_target feature without modeling and generalizing anything.
## Rules to avoid leakage
1) Use pipelines
2) Use arguments to skip one column during OHE
3) Check importances of features for trained models 
## Quick fix example
Instead of
```python3
X_train, y_train = (
    cc_apps_train_cat_encoding.iloc[:, :-1].values,
    cc_apps_train_cat_encoding.iloc[:, [-1]].values,
)
```
skip the column that was wrongly left during OHE
```python3
X_train = cc_apps_train_cat_encoding.iloc[:, :-2].values
y_train = cc_apps_train_cat_encoding.iloc[:, [-1]].values
```
## Test
[ohe_target_as_feature.py](/src/leakage_tests/ohe_target_as_feature.py)
## Incorporation stage
Modeling
## Locate in code 
Fit, separation on target and features
## Was met or loosely based on
[datacamp "Predicting Credit Card Approvals" project](https://app.datacamp.com/learn/projects/1908)
