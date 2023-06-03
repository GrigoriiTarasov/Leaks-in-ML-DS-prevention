## Effect
Overesteemed results.
## Rules to avoid leakage
Clearly check that test don't affect hyperparameter search etc. and used only for final estimation of model perfomance.
## Symptom
Test usage more than only for final estimation of model perfomance.
## Incorporation stage
Modeling
## Locate in code 
Fit/train code and anywhere where test is used not exclusevly for final estimation of model perfomance.
## Was met or loosely based on
[stackoverflow question on early stopping for LGBM](https://stackoverflow.com/questions/71579403/lightgbm-sklearn-api-doesnt-play-well-with-sklearns-gridsearch-if-you-want-ear)
