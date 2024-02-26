## 2.1 - Approaches to Self-Driving

sensory input -> mapping function -> steer

the goal is to find a mapping function that does the job very robustly and reliably

dominating paradigms:

- modular pipelines 
- end-to-end learning (imitation learning, reiforcement lering)
- direct perception

### modular pipeline

most dominating paradigm

mapping function:

1. low-level perception (extracting fundamental visual cues and characteristics without explicitly interpreting their semantic meaning. object detection)
2. scene parsing (integrate detected objects into a scene wrt the agent)
3. path planning
4. vehicle control

pros:

- small components, easy to develop in parallel
- interpretable

cons:

- piece-wise training (not jointly)
    - not all objects are equally important:
    - detect distant objects that are not relevant
    - example: parked cars 
- localization and planning heavily relies on HD maps

HD maps: centimeter precision lanes, markings, traffic lights/signs. human annotated 

### end-to-end

simplest and most promising

mapping function:

- neural network (imitation learning / reinforcement learning)

pros:

- end-to-end training
- cheap annotations

cons:

- training/ generalization
- interpretability

### direct perception

mapping function:

- neural network
- intermediate representations
- vehicle control

pros:

- compact representations
- interpretability

cons:

- control typically not learned jointly
- how to choose representations?

## 2.2 - Deep Learning Recap

### supervised learning

learning task

inference task

linear classification

logistic regression

multi-layer perceptron 

for classification problems 

- we use sigmoids or softmax non-linearty
- we use (binary) cross-entropy loss

for regression problems 

- we can directly return the value after teh last layer
- we use L1 or L2 loss

activation function 

convolutional neural networks 

## 2.3 - Imitation Learning



## 2.4 - Conditional Imitation Learning

there are some scenarios when imitation learning is not enough

in addition to the state we provide as an input an additional signal that tells the agents what should happen at the next intersection

neural attention fields


summary

advantages of imitation learning

- easy to implement
- cheap annotation 
- entire model trained end-to-end
- conditioning removes ambiguity at intersections

challenges of imitation learning

- behavior cloning uses IID assumption which is violated in practice
    - TODO: what is IID?
- direct mapping from images to control => no long term
- no memory (can't remember speed signs, etc) 
- mapping is difficult to interpret ("black box"), despite visualization techniques