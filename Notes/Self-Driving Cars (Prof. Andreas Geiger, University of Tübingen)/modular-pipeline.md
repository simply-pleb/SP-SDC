1. low level perception scene and parsing
    - input: sensory data
    - output: perception stack
        - Roadmap (road network definition)
        - Perception (agents, obstacles, signage)
        - Estimated pose and colision free space
        - Estimate of vehicle state
    - lec 7-11
        - Odometry, SLAM and localization
        - Road and lane detection
        - Reconstruction and motion
        - Object detection
        - Object Tracking
2. decision making and path planning
    - input: perception stack
    - output: path or trajectory
    - lec 12
        - route, behavior and motion planning
3. vehicle control
    - input: path or trajectory ?and estimate of vehicle state?
        - path does not specify velocity
        - trajectory explicitly considers time
    - output: steering, throttle, brake
    - lec 5, 6
        - vehicle dynamics (physical model of the agent)
        - vehicle control



PI Controller for Longitudinal Speed and Stanley Controller for lateral control.



MPC control horizon prediction horizon
- minimum of 2-3 steps for CH and CH should be 10-20% of PH

Linear MPC, Adaptive MPC, Gain-scheduled MPC, Non-linear MPC, Explicit MPC