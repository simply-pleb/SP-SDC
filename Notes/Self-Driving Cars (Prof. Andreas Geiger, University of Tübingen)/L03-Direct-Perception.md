# direct perception

mapping function:

1. neural network
2. intermediate representation
3. vehicle control

idea of direct perception

- hybrid model between imitation learning and modular pipelines
- learn to predict interpretable low-dimensional intermediate representation
- decouple perception from planning and control 
- allows to exploit classical controllers or learned controllers 

affordances

- attributes of the environment that limit space of actions
- in "this" case 13 affordances 

example of an early architecture:

- simulator -> shared memory -> CNN -> driving controller 
- TORCS simulator: open source car racing simulator 
- Network: AlexNet (5 conv layers, 4 fully connected layers), 13 output neurons (affordances?)
- Training: Affordance indicators trained with $\mathcal{l}_2$ loss

controller:

- steering controller: $s = \thata_1 (\alpha - d_c/w)$
    - $s$ steering command
    - $\theta_1$ parameter
    - $\alpha$ relative orientation
    - $d_c$ distance to center line
    - $w$ road width
- speed controller: $v =v_{max}(1 - \exp{(-\theta_2 d_p - \theta_3)})$
    - $v$ target velocity
    - $v_{max}$ maximal velocity
    - $d_p$ distance to preceding car
    - $\theta_{2,3}$ parameters

## conditional affordance learning

affordances

- distance to center line
- relative angle to the road
- distance to the lead vehicle
- speed signs 
- traffic lights
- hazard stop

## visual abstraction

intermediate representation improve perception

- depth
- optical flow
- semantic segmentation
- albedo

what is a good visual abstraction

- invariant (hide irrelevant variations from policy)
- universal (applicable to wide range of scenarios)
- data efficient (in term of memory/computation)
- label efficient (requires little manual effort)

semantic segmentation

- encodes task-relevant knowledge (e.g. road is drivable) and priors (e.g. grouping)
- can be processed with standard 2D convolutional policy network

disadvantages

- labelling time: ~90 min for 1 Cityscapes (what is Cityscapes?) image 

Questions

- what is the tradeoff between annotation time and driving performance?
- can selecting specific semantic classes ease policy learning?
- are visual abstractions trained with few images competitive?
- is fine-grained annotation important?
- are visual abstraction able to reduce training variance?

### label efficient visual abstractions

TODO: fill the following

model 

dataset

training

finely annotated classes vs coarsely annotated classes

- pixel accurate (finely) annotation requires more computational time
- using boxes (coarse) to annotate classes requires less computational time and does not perform worse 

privileged vs inferred classes 

Most relevant classes to annotate

- removing lane markings decreases performance
- 6 class representation performs better than 14 class representation 

## driving policy transfer 

we have seen how intermediate representation happened to be useful to decouple perception from planning and control in order to make policy learning easier

not all hardware is equivalent, so it might be useful to also decouple control from planning

problem:

- driving policies learned in the simulator do not transfer well to the real world

idea:

- encapsulate driving policy such that it is not directly exposed to raw perceptual input or low-level control (input: semantic segmentation, output: waypoints)
- allows for transferring driving policy without retraining or finetuning

representations:

- input: semantic segmentation (per pixel "road" vs "non-road")
- output: 2 waypoints (distance to vehicle, relative angle wrt vehicle heading)
    - one waypoint will be sufficient for steering and the other is used for breaking before turns
    - and there is a PID controller that tries to follow the lane based on the waypoints

model used in some paper:

- driving policy: conditional imitation learning
- controller: PID controller for lateral and longitudial control
- results: full method generalizes best ("+" = with data augmentation)

## online vs offline evaluation

- online evaluation (i.e., using a real vehicle) is expensive and can be dangerous
- offline evaluation on a pre-recorded validation dataset is cheap and easy
    - measure error to the ground truth
- question: how predictive is offline evaluation to the online task?

online metrics used

- success rate: percentage of routes successfully completed
- average completion: average fraction of distance to goal covered
- km per infraction: average driven distance between 2 fractions 

offline metrics used

- offline metrics are regularly proxies to the online metrics
- online and offline metrics tend to be not very well correlated

--- 

Summary

- direct perception predicts intermediate representations
- low-dimensional affordances or classic classic computer vision representations (e.g., semantic segmentation, depth) can be used as intermediate representations
- decouples perception from planning and control
- hybrid model between imitation learning and modular pipeline
- direct methods are more interpretable as the representations can be inspected
- effective visual abstractions can be learned using limited supervision
- planning can also be decoupled from control for better transfer 
- offline metrics are not necessarily indicative of online driving performance 