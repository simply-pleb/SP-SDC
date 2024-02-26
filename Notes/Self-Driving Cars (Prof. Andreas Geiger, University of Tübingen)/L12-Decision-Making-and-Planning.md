# Decision Making and Planning 

Problem definition:

- goal: find and follow path from current location to destination
- take static infrastructure and dynamic objects into account 
- input: vehicle and environment state (via perception stack)
- output: path or trajectory as input to vehicle controller

challenges:

- driving situation and behavior are very complex
- thus difficult to model as a single optimization problem
- idea: break planning problem into a hierarchy of simpler problems
    - route planning
        - input: user specified destination
        - observed: road map (road network definition)
        - output: waypoints
    - behavior planning
        - input: waypoints
        - observed: perception (agents, obstacles, signage)
        - output: motion specification
    - motion planning
        - input: motion specification
        - observed: estimated pose and collision free space
        - output: path or trajectory
    - local feedback control
        - input: path or trajectory
        - observed: estimate of vehicle state
        - output: steering, throttle, brake
        - already discussed in lecture 5-6

## Route planning

BFS

Dijkstra Shortest path

Euclidean Planning heuristics

A*

## Behavior planning 

Behavior planning

- behavior planning stage discretizes the behavior into simpler (atomic) maneuvers, each of which can be addressed with a dedicated motion planner
- the behavior planner must take into account traffic rules, static and dynamic objects
- input: high-level route plan and output of perception stack
- output: motion planner constraints: corridor, objects, speed limits, targets, ... 
- frequently used models:
    - deterministic: Finite State Machine (FSMs) and variants
    - probabilistic: Markov Decision Process 

Hierarchical State machine

## Motion planning

- path does not specify velocity
- trajectory explicitly considers time

main formulations:
- variational models
- graph search methods
- incremental search techniques