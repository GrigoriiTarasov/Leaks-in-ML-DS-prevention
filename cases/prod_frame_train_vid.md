## Effect
Overesteemed results by a model that restores video and make prediction as a whole.
However, its performance significantly drops when it operates in an online regime, predicting one frame at a time.
## Rules to avoid leakage
Represent data for training in same modality as it will be inferenced in production,
if each frame need to be predicted stratify train dataset to break the ability to interpolate prediction from frames inaccesible in production mode of work.
## Incorporation stage
Ground truth gathering.
Dataset preparation.
## Locate in code 
Сroping on frames, selection which frames to include in train dataset
## Was met or loosely based on
[kaggle "State Farm Distracted Driver Detection" competition JACOBKIE solution](https://www.kaggle.com/c/state-farm-distracted-driver-detection/discussion/22906)
