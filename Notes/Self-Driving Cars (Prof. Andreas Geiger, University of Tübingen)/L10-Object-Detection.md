how to measure detection performance

- average precision metric:
    1. run detector with varying thresholds
    2. assign detections to closest object (bipartite graph matching: Hungarian algorithm)
    3. count TP, FP, FN
        - TP: number of objects correctly detected (IoU Intersection over Union > 0.5)
        - Precision         P
        - Recall            R
        - Average Precision AP


Sliding Window Object Detection


Region based CNN


proposal based object detection

- Naïve idea: classify all possible boxes in the image using a classification network
- Problem: too many boxes to classify (even if space is discretized)
- better idea:
    - **detect** ~2k candidate bounding boxes that might contain an object (quantize) => choose set such that it is overcomplete (i.e. it should contain all boxes)
    - **classify and refine** the location of boxes using a deep neural network (regress)
- this approach is called a proposal-based (2-stage) object detection
- note: we have split the original object detection problem into 2 proxy tasks
- apprximation with finite set of boxes leads to quantization error (quantize) 
- recover loss of localization accuracy by regressing the location offset (regress)
- remove redundant predictions using non-maximum-suppression (clustering)

R-CNN


fast R-CNN

faster R-CNN

feature pyramid network

- goal: improve scale equivariance
- detector needs to classify and localize objects over a range of scales


masked r-cnn

densepose

mesh r-cnn

Foreground-Background Imbalance 

single stage detection

- YOLO and SSD: Alternative to proposal-based pruning of output space
- Regress boxes and predict class probability in single stage at 7x7 locations
- Faster, but worse performance due to dramatic subsampling of output space (large quantization error hard to correct in practice => low AP)




## Performance evaluation

## Sliding window object detection

## Region based CNN

## 3D Object Detection