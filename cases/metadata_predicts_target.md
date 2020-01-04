## Effect
Overesteemed results.

"Baseline" exploiting leakerage predicts test by metadata achieving good score without modeling and generalizing anything.
## Symptom
The distribution of the target varies significantly across metadata
## Rules to avoid leakage
Mutually exclusive options are
1) Stratify data so that metada equally distributed among the target variable.
2)  Cut the metadata in an irretrievable manner, providing only those features that are valid to be used during inference in production.

Anti-pattern: restrict usage of all the metadata. The modelers always highlights that height and width are considered as metadata for images and it always is used during train.
## Incorporation stage
Ground truth gathering.
Dataset preparation.
## Locate in code 
Saving train dataset
## Was met or loosely based on
[kaggle "Deepfake Detection Challenge" competition zaharch post](https://www.kaggle.com/code/zaharch/data-leak-in-metadata)
