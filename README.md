# Data leaks during modeling in ML and DS system detection, mitigation, prevention ongoing Handbook
## 1. Scope
This project is about data leaks in Machine Learning/Data Science (ML/DS) systems that 
occurs due to errors in experiment design, data preparation, data modeling  which can affect the final predictive system by lowering its generalization capabilities and/or skewing performance estimations. 
Simply put, such leaks can lead to inflated performance metrics for models that actually have lower predictive power when deployed.

Out of scope:
1) SecurityOps: Breaches and raw data exposure e.g. unsecured accounts
2) Membership inference, reference, popultion
3) ML competition specific metric probing/abuses and platform related abuses

Adversarial prompt attacks are in scope.

## 2. Aim

The goal of this project is to provide a comprehensive table for practitioners of potential data leaks in ML/DS systems, along with best practices for avoiding them, quick-fix examples, and, where possible, tests to check if data is affected by such leaks. 
The cases are sourced from both competitions and practical scenarios, with links to discussions or sources provided where possible. The material about errors in DS research papers is in [Leakage and the reproducibility crisis in machine-learning-based science Sayash Kapoor, Arvind Narayanan](https://arxiv.org/abs/2207.07048) it concentrates more on taxonomy without technical details like SIFTs in this repository.

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
| 8 | [Target can be predicted by metadata](/cases/metadata_predicts_target.md)  | Overesteemed results | The distribution of the target varies significantly across metadata | ground truth gathering<br>dataset preparation | Train test split | [kaggle "Deepfake Detection Challenge" competition zaharch post](https://www.kaggle.com/code/zaharch/data-leak-in-metadata) |
| 9 | [Test intersects train](/cases/test_intersect_train.md) | Overesteemed results | Identical rows between test and train | dataset preparation | Train test split and/or duplicate check | [kaggle "Arxiv Title Generation" competition YURY KASHNITSKY post](https://www.kaggle.com/code/kashnitsky/arxiv-title-generation-dumb-baseline) |
| 10 | [Recoverable/restorable/de-anonymizable features, objects when it's not intended](/cases/recoverable_features_objs.md) | Exposure of private data possible/no such data field during production | - | dataset preparation | anonimization, encoding | [kaggle "Optiver Realized Volatility Prediction" competition nyanpn comment](https://www.kaggle.com/competitions/optiver-realized-volatility-prediction/discussion/274970#1526988) |
| 11 | [Evaluation intersect test<br>e.g. early stoping on test](/cases/test_based_evaluation.md) | Overesteemed results | Test usage more than only for final estimtion of model perfomance | modeling | Fit/train code | [stackoverflow "LightGBM eval question"  paperskilltrees comment](https://stackoverflow.com/a/71581716/7607734) |
| 12 | [OHE 1-target](/cases/ohe_target_as_feature.md) | No generalization | 100% on trian and error on new data | modeling | Check train/fit code | [datacamp "Predicting Credit Card Approvals" project](https://app.datacamp.com/learn/projects/1908) |
| 13 | [Adversarial prompt attacks](/cases/adversarial_prompt_attacks.md) | Overestimated score | Cosine similarity is used e.g. for prompt recovery quality estimation | ML task setting: metric choice for model scoring |  | [kaggle "LLM Prompt Recovery" competition KHOI NGUYEN solution](https://www.kaggle.com/competitions/llm-prompt-recovery/discussion/494343) |

## 5. Rights
This project is currently unsponsored and not affiliated with any institution. 
For inquiries about incorporating it into your program or publication, please contact grigoriy.tarasov.u@gmail.com.