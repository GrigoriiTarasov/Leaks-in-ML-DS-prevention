## Effect
Overesteemed results
## Rules to avoid leakage
Check if stratification is done right in case of non-independent individual samples e.g. grouped samples, exist rows that are observations about same one object
## Symptom
Observation about same object present in different splits e.g. sample with same group-id is present present in at least two of [train,val,test] 
## Quick fix example
```python3
# define feature that reflect group: grouping_feature

from sklearn.model_selection import GroupShuffleSplit 

splitter = GroupShuffleSplit(n_splits=2, 
							 test_size=0.2, 
							 random_state = 42)
split = splitter.split(df, 
					   groups=df[grouping_feature])
train_inds, test_inds = next(split)

train = df.iloc[train_inds]
test = df.iloc[test_inds]
```
## Test
[group_strat.py](/src/leakage_tests/group_strat.py)

## Incorporation stage
Dataset preparation.
Modeling.
## Locate in code 
Split and save of validation and/or test part of dataset.
## Was met or loosely based on
[kaggle "TalkingData Mobile User Demographics" Laurae comment](https://www.kaggle.com/competitions/talkingdata-mobile-user-demographics/discussion/23403#134437)
