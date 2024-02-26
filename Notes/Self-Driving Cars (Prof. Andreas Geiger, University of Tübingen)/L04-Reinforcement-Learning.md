# Reinforcement learning

## Markov decision process

## Bellman optimality and Q-Learning

state-value function

action-value function

optimal state-value function

TODO: understand Q-learning

update sequence $Q_1, Q_2, ...$ using learning rate $\alpha$:

$$Q_{i+1}(s_t, a_t) = Q_i(s_t, a_t) + \alpha(r_t + \gamma\max_{a' \in \mathcal{A}}Q_i(s_{t+1}, a') - Q_i(s_t, a_t))$$

- target: $r_t + \gamma\max_{a' \in \mathcal{A}}Q_i(s_{t+1}, a')$
- prediction: $Q_i(s_t, a_t)$ 
- $Q_i$ will converge to $Q^*$ as $i \rightarrow \infty$
- Note: policy $\pi$ learned implicitly via Q table

## Deep Q-learning

deep Q-learning using experience replay and fixed Q targets

- take action $a_t$ according to $\epsilon$-greedy policy
- store transition $(s_t, a_t, r_t, s_{t+1})$ in replay memory $D$
- sample random mini-batch of transitions $(s_t, a_t, r_t, s_{t+1})$ from $D$
- compute $Q$ targets using old parameters $\theta^-$
- optimize MSE between Q targets and Q network predictions $$\mathcal{L}(\theta) = \mathbb{E}_{s_t, a_t, r_t, s_{t+1} \sim D} \left[\left(r_t + \gamma \max_{a'}Q(s_{t+1}, a'; \theta^-) - Q(s_t, a_t; \theta)\right)^2\right]$$ using stochastic gradient descent 


deep Q learning shortcomings 

- long training time 
- uniform sampling from replay buffer $\Rightarrow$ all transitions equally important 
- simplistic exploration strategy  
- relies on fully observable states
- action space is limited to a discrete set of actions

various improvements over the original algorithm have been explored 

Deep Deterministic Policy Gradients

- DDPG addresses the problem of continuous action space
- Problem: finding a continuous action requires optimization at every timestep
- Solution: use two networks, an actor (deterministic policy) and a critic
- Actor: $s \rightarrow \theta^\mu \rightarrow \mu(s;\theta^\mu)$
    - Actor network with weights $\theta^\mu$ estimates agent's deterministic policy $\mu(s; \theta^\mu)$
    - update deterministic policy $\mu(\cdot)$ in direction that most improves $Q$
    - apply chain rule to the expected returns (this is the policy gradient): $$\nabla_{\theta^\mu}\mathbb{E}_{s_t, a_t, r_t, s_{t+1} \sim D}\left[Q(s_t, \mu(s_t; \theta^\mu); \theta^Q)\right] = \mathbb{E}\left[\nabla_{a_t}Q(s_t, a_t; \theta^Q)\nabla_{\theta^\mu}\mu(s_t;\theta^\mu)\right]$$
- Critic: $s \text{ and } a=\mu(s;\theta^\mu) \rightarrow \theta^Q \rightarrow Q(s, a; \theta^Q)$
    - critic estimates value of current policy $Q(s,a;\theta^Q)$
    - learned using the Bellman Optimality Equation as in Q learning: $$\nabla_{\theta^Q} \mathbb{E}_{s_t, a_t, r_t, s_{t+1} \sim D}\left[\left(r_t + \gamma Q(s_{t+1}, \mu(s_{t+1}; \theta^{\mu-});\theta^{Q-}) - Q(s_t, a_t; \theta^Q)\right)^2\right]$$
    - remark: no maximization over actions required as the step is now learned via $\mu(\cdot)$
- experience replay and target networks are again used to stabilize training 
    - replay memory $D$ stores transition tuples $(s_t, a_t, r_t, s_{t+1})$
    - target networkds are updated using "soft" target updates
    - weights are not directly copied but slowly adapted:
        - $\theta^{Q-} \leftarrow \tau\theta^Q + (1-\tau)\theta^{Q-}$
        - $\theta^{\mu-} \leftarrow \tau\theta^\mu + (1-\tau)\theta^{\mu-}$
        - where $0 < \tau << 1$ controls the tradeoff between speed and stability of learning 
- exploration is performed by adding noise (correlated noise) to $\nabla_{\theta^\mu}$ to the policy $\mu(s)$: $$\mu(s;\theta^\mu) + \mathcal{N}$$
- prioritize experience to replay important transitions more frequently 
    - priority $\delta$ is measured by magnitude of temporal difference (TD) error: $$\delta = | r_t + \gamma \max_{a'}Q(s_{t+1}, a'; \theta^{Q-}) - Q(s_t, a_t; \theta^Q) |$$
    - TD error measures how "surprising " or unexpected the transition is 
    - Stochastic prioritization avoids overfitting due to lack of diversity
    - Enables learning speed-up by a factor of 2 on Atari benchmark

Asynchronous Deep Reinforcement Learning

Bootstrapped QDN

Double Q-learning

Deep recurrent Q-learning (replace linear layer with LSTM)


Summary

- Reinforcement learning learns through interaction with the environment
- The environment is typically modeled as a Markov Decision Process
- The goal of RL is to maximize the expected future reward
- Reinforcement learning requires trading off exploration and exploitation
- Q-learning iteratively solves for the optimal action-value function 
- the policy is learned implicitly via Q table
- Deep Q-learning scales to continuous/high-dimensional state spaces
- Deep deterministic policy gradients scales to continuous action spaces 
- experience replay and target networks are necessary to stabilize training