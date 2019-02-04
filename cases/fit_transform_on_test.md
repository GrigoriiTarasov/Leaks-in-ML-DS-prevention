## Effect
Overesteemed results.
## Rules to avoid leakage
1) Clearly separate train and test dataset
2) Use pipelines for fit_transform and transform
## Quick fix example
```python3
X_train_transformed = pipeline.fit_transform(X_train)
X_test_transformed = pipeline.transform(X_test)
```
## Incorporation stage
Modeling.
## Locate in code 
Change of test data prior training
