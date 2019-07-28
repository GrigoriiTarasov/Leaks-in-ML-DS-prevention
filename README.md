# Data leaks during modeling in ML and DS system detection, mitigation, prevention ongoing Handbook
## 1. Scope
This project is about data leaks in Machine Learning/Data Science (ML/DS) systems that 
occurs due to errors in experiment design, data preparation, data modeling  which can affect the final predictive system by lowering its generalization capabilities and/or skewing performance estimations. 
Simply put, such leaks can lead to inflated performance metrics for models that actually have lower predictive power when deployed.

## 2. Aim

The goal of this project is to provide a comprehensive table for practitioners of potential data leaks in ML/DS systems, along with best practices for avoiding them, quick-fix examples, and, where possible, tests to check if data is affected by such leaks. 
The cases are sourced from both competitions and practical scenarios, with links to discussions or sources provided where possible.

## 3. Code

### 3.1 Tests
[./src/leakage_tests/](/src/leakage_tests/)
contains function in python with assert statments free of binding to particular test library. 
Modification to your own case are meant.

### 3.1 Quick-fixes
Some of 
./cases/*.md
contains examples of particular lines replacment to exterminate the data leak.

## 4. Table of  leaks summaries


| id | name and detail link | effect | symptom | stage | locate in code |  met or loosely based on |
| -- | -- | --- | --- | ---- | --- | --- |
| 1 | [Restorable vids in train<br>but frames in prod](/cases/prod_frame_train_vid.md) | Overesteemed results |  - | ground truth gathering<br>dataset preparation | croping on frames | [kaggle "State Farm Distracted Driver Detection" competition JACOBKIE solution](https://www.kaggle.com/c/state-farm-distracted-driver-detection/discussion/22906) |
| 2 | [Records about same object<br>in train and test](/cases/insufficient_stratification.md) | Overesteemed results  | Observation about same object present in different splits e.g. sample with same group-id is present present in at least two of [train,val,test] | dataset preparation<br>modeling | Separation on validation sets | [kaggle "TalkingData Mobile User Demographics" Laurae comment](https://www.kaggle.com/competitions/talkingdata-mobile-user-demographics/discussion/23403#134437) |
| 3 | [id is sorted by target<br>or smth other unrevealed in production](/cases/id_sort_leak.md) | Exploits of ranking<br>preditions using information<br>from ids |  | dataset preparation | Dataset saving |  |
| 4 | [fit_transform on whole<br>instead of train](/cases/fit_transform_on_test.md) | Overesteemed results |  | modeling | test transform |  |
| 5 | [Time aviabilitiy of feature<br>initialy not satisfied](/cases/time_aviabilitiy_initial.md) | Non-adequate predictions  | If the feature obviobly aviable<br>later then the moment it refered in dataset | dataset<br>preparation | Feature aggregation<br>assigning to time axis |  |
| 6 | [Taking information<br>from future during the modeling](/cases/ts_val_leak.md) | Overesteemed results |  | modeling | Separation on validation sets |  |
| 7 | [Test intersects train resolvable by search in features space](/cases/test_match_restore_embed_search.md) | Overesteemed results | Dataset is looking like already augmented contating many versions of same e.g. pictures, audio pieces | ground truth gathering<br>dataset preparation | Choice of which image/audio/etc. pieces to include in train and final test | [kaggle "Airbus ship detection" competition ANDRÉS MIGUEL TORRUBIA SÁEZ post](https://www.kaggle.com/competitions/airbus-ship-detection/discussion/64355) |