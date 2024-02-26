ego-motion - own motion of the car

3 types of motion estimates

- visual odometry refers to the estimation of relative ego-motion from images 
- SLAM (simultaneous localization and mapping) algorithm build a map and simultaneously localize in that map
- Localization methods find the global pose of a vehicle in a given map

odometry and SLAM should be tackled jointly

## Visual odometry

- odometry is the use of sensors to estimate change in ego-position over time
- Greek origin: odos (route) and metron (measure)
- odometry yields relative motion estimates (not global position wrt. a map)
- it is hence sensitive to error accumulation over time (only precise locally) 

wheel odometry

- wheel odometry systems use wheel encoder to measure wheel rotation
- inertial measurement units measure a body's forces (acceleration)
- visual odometry algorithms use camera images 

indirect vs direct visual odometry 

- 
- input images layer
- indirect methods have feature detection, extraction and matching layer in between. also called feature based visual odometry  
- track and map layer in indirect method
    - track: min. projection error (point distances)
    - map: estimate keypoint parameters (f.e. 3D coordinates)
- track and point layer in direct method
    - track: min. photometric/geometric error pixel-wise
    - map: estimate per-pixel depth from photoconsistency

### Indirect visual odometry

extract and match keypoints

- extract blobs and corners 
- detect salient points in the image (blobs, corners) and extract local features
- features should be invariant to perspective and illumination changes
- many option (some are faster than others): SIFT, SURF, U-SURF, BRISK, ORB, FAST
- match features between two images by their similarity (correspondences)  

### image formation process

perspective projection

calibration matrix $K$

- the parameters of $K$ are called camera intrinsics  

chaining transformations

### epipolar geometry

epipolar line 

epipolar plane

epipolar constraint

essential matrix matrix

non linear optimization 
- minimize reprojection error

stereo visual odometry

### direct visual odometry

direct sparse odometry


indirect vs direct methods

- direct methods often lead to more accurate results as they exploit the full image
- however, satisfying real-time requirements requires efficient implementations 
- furthermore, they suffer from local minima and require accurate initialization
- feature-based methods are faster, but in general less accurate
- this is because only few reliable feature correspondences can be found
- however, they are more robust to initialization and less prone to local minima
- thus, both techniques are combined (e.g., using features to initialize pose that is then finetuned using a direct method) 

## SLAM (simultaneous localization and mapping)

- so far: optimization of 2 adjacent frames, no focus on map
- now: optimize over large windows (ideally entire history)
- we optimize both poses and map (e.g., 3D feature localization)
- SLAM is a chicken-egg problem (localization requires mapping and vice-versa) $\Rightarrow$ joint optimization of poses and map is necessary 
- key feature of SLAM: correct accumulation errors via loop-closure detection
- the resulting map can be used for localization 
- there exists indirect (feature-based) and direct SLAM methods
- Many flavors: EKF SLAM, Bundle Adjustment, Windowed BA, ... 

bundle adjustment 

loop closure detection

indirect SLAM methods

direct SLAM methods

## Localization 

### Satellite localization

Trilateration

- we need a minimum of 4 satellites in order to be "visible"

problems with satellite localization

- availability
    - satellites not visible in tunnels, narrow city streets
    - dependency on national organizations / interests
- accuracy
    - 5m - 15m for GPS and 0.5m-5m for DGPS (differential)
    - only location, no rotation (not full pose)
- frequency
    - max 5-10 Hz
    - we need around 500 Hz to fully control a vehicle
- atmospheric variation (lead to errors)
    - Can be partially corrected by DGPS using signals from nearby base station
- DGPS requires communication and initialization
- Multipath effects (wrong signals due to reflections, e.g., at facades)

### Visual localization

topometric localization

- setup: record sequences with cameras, Lidar and GPS as ground truth
- goal: localize new images (different day/season) wrt recorded sequences
- combines metric and topological localization
    - metric: optimize pose wrt. feature correspondences 
    - topological: estimate observer location qualitatively from finite set of locations
    - here: describe image with global feature vector; align query with recorded sequence
    - however, only localize wrt. node (=frame) in graph (no full 6D pose)

- map creation
    - directed graph, nodes (=frames) created based on distance threshold 
    - feature: SURF applied to whole image (64D) + average/std.dev. of range scan 
- bayesian localization
    - predict: 
    - update: 
    - with:
        - motion model
        - measurement model
        - location
        - note: strictly speaking this formulation handles tracking, but not localization

Visual localization: Learning-based localization 

- PoseNet

Visual localization: Feature-based localization 

- overview
    - 
- mapping
- descriptor matching
    - popular approachs: k-d trees, inverted index
- pose estimation
- geometric verification

Map-based localization

---

summary

- visual odometry estimates relative ego-motion from images
- SLAM algorithms build a map and simultaneously localize in that map
- SLAM algorithms use loop closure detection to close loops
- Localization methods find the global pose in a given map 
- Indirect and direct VO/SLAM methods exist
- Indirect methods are faster and converge better, but are less accurate
- Direct methods are slower but lead to more accurate results
- Direct and indirect methods can be advantageously combined
- Except for offline mapping, real-time computation is required