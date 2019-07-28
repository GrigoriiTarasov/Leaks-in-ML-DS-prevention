## Effect
Overesteemed results.

"Baseline" exploiting leakerage that only provides matching between test and train has no error on intersection without modeling and generalizing anything.
[examples_im_for_embed_search.png](./examples_im_for_embed_search.png)
## Rules to avoid leakage
 Create stratification rules that will exclude images from test that matches similiar in test.
## Search of duplicates
Can use [LoFTR Detector-Free Local Feature Matching with Transformers](https://kornia.github.io/tutorials/nbs/image_matching.html) as end-to end solution or
generate some SIFT/histogram features/embeddings and then search by Approximate Nearest Neighbors (ANNOY) or KDTrees, for example


```python3
def get_potential_duplicates_by_embed(test_embs, train_embs, threshold=0.1, tree_size=50)->dict:
  """
  Finds nearest neighbors for each test embedding in test_embs within train_embs.

  Args:
      test_embs: A list of test embeddings.
      train_embs: A list of train embeddings.
      threshold: Distance threshold for considering a neighbor as nearest.
      tree_size: Number of trees to use in the Annoy index.

  Returns:
      A dictionary where keys are indexes from test_embs and values are the nearest neighbor's id from train_embs
      if the distance is below the threshold.
  """

  t = AnnoyIndex(len(train_embs[0]), "angular")
  for idx, x in enumerate(train_embs):
    t.add_item(idx, x)
  t.build(tree_size)

  nn_dict = {}
  for i, test_emb in enumerate(test_embs):
    nn_id, nn_distance = t.get_nns_by_item(i, 1)[0]
    if nn_distance < threshold:
      nn_dict[i] = nn_id
    else:
      nn_dict[i] = None

  return nn_dict
```

## Incorporation stage
Ground truth gathering should account that that test set images must contain images that can't be matched from images from train dataset e.g. don't treet close/overlapping frame as an independent sample.
Dataset preparation must stratify samples to be independend.
## Was met or loosely based on
[kaggle "Airbus ship detection" competition ANDRÉS MIGUEL TORRUBIA SÁEZ post](https://www.kaggle.com/competitions/airbus-ship-detection/discussion/64355)

