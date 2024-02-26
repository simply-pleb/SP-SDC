# Object Tracking

elements of tracking

- detection: where are candidate objects in each frame 
- association: which detection corresponds to which object
- filtering: what is the most likely object state, e.g., location and size (detections are noise -> exploit probabilistic observations/motion models)

online vs offline tracking   

- online tracking: estimate current state given current and past observations
- offline tracking: estimate all states given all observations (batch mode)
- as we consider self-driving, we will focus on oline tracking 

## Filtering 

state vs observation

- hidden state: parameters of interest (e.g. object location)
- observation: what we directly observe (= measurement)
- due to sensor noise/observability: hidden state != observation

general assumptions

- camera is not moving instantly to a new viewpoint
- objects do not disappear and reappear in different place
- gradual change in pose between camera and scene
- bayesian filter assumes that the state follows Markov process
- we have a hidden markov state
    - $x_t \in \mathbb{R}^M$ denotes true hidden state at time $t$
    - $y_t \in \mathbb{R}^N$ denotes some noisy measurement of $x_t$ at time $t$

Bayes filter

- two alternating steps:
    - prediction: predict where the object should be in the next step 
    - correction: correct prediction based on current observation
- Prediction: TODO: add formulation
- Correction: TODO: add formulation

Kalman filter

- if $p(x_t | x_{t-1})$ and $p(y_t | x_t)$ are linear and normally distributed, we obtain the Kalman filter (KF) -> parameters: mean $\mu$ / covariance $\Sigma$
- the solution for the Kalman filter is given in close form as products/margins are Gaussian -> max. likelihood = least squares
- the Kalman filter is the optimal linear filter in least squares sense
- non linear cases: Extended Kalman Filter (EKF), Unscented Kalman Filter (UKF)

Examples: linear cases

- constant velocity 
- constant acceleration

## Association

multi-object tracking

- algorithm
    - predict objects from previous frame and detect objects in current frame
    - associate detections to object tracks (initiate/delete tracks if necessary)
    - correct predictions with observations (e.g., Kalman filter)
- when do observations in consecutive frames belong together
    - predict bounding box (via motion model) and measure overlap
    - compare color histograms or normalized cross-correlation
    - estimate optical flow and measure agreement
    - compare relative location and size of bounding box
    - compare orientation of detected objects

metric learning

- triplet loss

correspondence ambiguities

nearest neighbor association

bipartite graph matching

- integer linear program
- augment the matrix by adding a threshold that will account for tracks that end

graph based tracking

- cast as min-cost flow network problem
- successive shortest path algorithm

advanced graph model 

multi-object tracking evaluation

- associate predictions with ground truth tracks
- MOTA: Multi Object Tracking Accuracy
- HOTA: High Order metric for evaluating multi-object Tracking Accuracy

KITTI benchmark

## Holistic scene understanding

probabilistic graphical model

PnPNet: Perception and Prediction with tracking in the loop

Argoverse: 3D tracking and forecasting with rich maps