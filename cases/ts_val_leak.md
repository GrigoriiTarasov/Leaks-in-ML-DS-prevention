## Effect
Overesteemed results.
## Rules to avoid leakage
Use time based validation if time axis is present in data.

Example: when the smallest unit of data availability spans multiple rows, a simple row-based split can leave data from the same day in both the train and test sets. This can cause the test set to appear better than it actually is because it contains data from the same day as the training set.
```python 
train_x, test_x, train_y, test_y = train_test_split(data, target, test_size=0.2,random_state=42)
```

Example of correct way in such case:
```python 
test_x = data[data['date_id'] >= 390]
train_x = data[data['date_id'] < 390]
test_y = target[data['date_id'] >= 390]
train_y = target[data['date_id'] < 390]
```


## Incorporation stage
Modeling.
## Locate in code 
Cross validation, spliting to train and test.
