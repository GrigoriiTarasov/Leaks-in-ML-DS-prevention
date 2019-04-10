## Effect
Non-adequate predictions
## Rules to avoid leakage
Three multiple exclusive approaches
1) Maintain a separate data source with the exact time of acquisition, allowing the modeler to combine it with other data as needed.
2) Check if time axis relibly reflects time when such data is observable.
3) Remove the column entirely if it is derived from future data and cannot be reliably linked to specific points in time.
## Symptom
If a feature/column is clearly available at a later time than the moment it is referenced in the dataset
## Incorporation stage
Dataset preparation.
## Locate in code 
Feature aggregation, assigning to time axis

