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