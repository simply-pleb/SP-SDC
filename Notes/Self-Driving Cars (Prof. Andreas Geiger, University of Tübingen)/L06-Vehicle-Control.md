# Vehicle control

open loop controller 

- hard to do in practice
- requires precise knowledge of the plant and the influence factors 
- no feedback about controlled variables
- cannot handle unknown disturbances, resulting in drift 

closed loop controller 

- introduces a sensor that takes measurements of the process and outputs them to the input (to the controller)
- calculates an error that we want to bring down to zero 
- a vehicle needs to be controlled both longitudinally and laterally 
- we consider 3 different types of controllers
    - black box controllers: dont require knowledge about the process
    - geometric controller: exploits geometric relationships between the vehicle and the path, resulting in compact control laws for path tracking
    - optimal controller: use knowledge of the system and minimize an objective function over future time steps

## Black box control

dont require knowledge about the process

bang-bang controller (the most simple form of a controller)

- also known as hysteresis controller
- often applied e.g. in household thermostats
- switches abruptly between two states
- mathematical formulation: $$u(t) = \begin{cases}u_1, \text{ if } e(t)\ge \tau \\ u_2, \text{ otherwise}\end{cases}$$


PID controller 

- the most common controllers in industrial applications
- comprises proportional (P), integration (I) and differential (D) elements (wrt to the error)
    - P: $K_p e(t)$
    - I: $K_i \int_0^t{e(t')dt'}$
    - D: $K_d \frac{de(t)}{dt}$
- mathematical formulation: $$u(t) = K_p e(t) + K_i \int_0^t{e(t')dt'} + K_d \frac{de(t)}{dt}$$ with parameters $K_p$, $K_i$ and $K_d$
- using the P element alone leads to overshooting / oscillation
- adding a D element alleviates this problem by introducing damping behavior
- the I element corrects residual errors by integrating past error measurements
- Ziegler-Nichols heuristics
    - set $K_i = K_d = 0$
    - increase $K_d$ until the ultimate gain $K_d = K_u$ where the system oscillates
    - measure oscillation period $T_u$ and $K_u$
    - set $K_p = 0.6K_d$, $K_i = 1.2K_u/T_u$ and $K_d = 3K_uT_u/40$

Longitudal vehicle control

- $v(t) = v_{max}(1 - \exp{(-\theta_1 d(t) -\theta_2)})$
- $v(t)$: target velocity at time t
- $d(t)$: distance to preceding car
- Reference variable: r(t) = v(t) = target velocity
- Correcting variable: u(t) = gas/brake pedal
- Controlled variable: y(t) = current velocity
- Error: e(t) = v(t) - y(t)

Lateral vehicle control

- reference variable: r(t) = 0 = no cross track error
- correcting variable: u(t) = $\delta$ = steering angle
- controlled variable: y(t) = cross track error
- error: e(t) = -y(t) = cross track error

PID control (waypoint based vehicle control)

- Example: waypoint based vehicle control
- Input: waypoints $w = {w_1, ..., w_K}$
- Velocity: (Longitudinal PID control) $$v = \frac{1}{K}\sum_{k=1}^K\frac{\|w_k - w_{k-1}\|_2}{\Delta t}$$ 
    - L2 distance
- Steering angle: (Lateral PID control) $$\delta = \tan^{-1}{\frac{p_y}{p_x}}$$
    - p - point at a circular arc that corresponds to the path drown by the waypoints

## Geometric control

pure pursuit control

- track a target point at lookahead distance $d$ to follow path
- exploit geometric relationship between the vehicle and the path to follow
- minimize the cross track error $e$ by following a circular trajectory
- streering angle $\delta$ determined by angle $\alpha$ between vehicle heading direction and lookahead direction. but what is $\delta(\alpha)$?
- $k = \dfrac{1}{R} = \dfrac{2\sin\alpha}{d}$, whith $k$ being the curvature of the trajectory
- $\delta \approx \dfrac{2L\sin\alpha}{d}$
    - $L$: distance between the two tires of the bicycle model  
    - $d$: lookahead distance
- $d$ is often based on the vehicle speed $v$
    - $d = Kv$ with constant $K$
- $\delta \approx \dfrac{2L}{d}e$

stanley control

- $\delta = \psi + \tan^{-1}\left(\dfrac{ke}{v}\right)$
- $v$ = speed, $\psi$ = heading error, $e$ = crosstrack error 
- reference at front axle, no lookahead
- combines heading and crosstrack error
- it can be shown that the crosstrack error converges exponentially 0 (independent of $v$)
- works for small velocities without disturbances 
- as heading changes, heading correction counteracts crosstrack correction
- the stanley controller can correct large crosstrack and large heading errors
- global stability: independent of initial conditions guides vehicle back (proven)
- but does not consider noisy observations, actuator dynamics, tire force effects
- softening/dampening terms and curvature information can be added

## Optimal control

both optimal and model predictive controllers make use of underlying dynamics

for these controllers we need a model 

linear quadratic regulator (LQR) 

- only applicable to linear systems 

model predictive control
- builds upon LQR while giving up on closed form solution requiring test time optimization (we optimize the function during the execution of our controller)
- more computationally expensive, but we gain modeling flexibility
- generalizes LQR to 
    - non-linear: cost function and dynamics (consider straight road leading into turn)
    - flexible: allowing for receding window and incorporation of constraints
    - expensive: non-linear optimization required at every iteration 
- formally: 
    - sum of consts: $\argmin_{\delta_1,...,\delta_T}{\sum_{t=1}^T{C_t(x_t, \delta_t)}}$
    - initialization: $s.t.\ \ x_1 = x_{\text{init}}$
    - dynamic model: $x_{t+1} = f(x_t, \delta_t) $
    - constraints: $\underline\delta \le \delta_t \le \overline \delta$
- unroll dynamic model $T$ times $\Rightarrow$ apply non-linear optimization to find $\delta_1, ... \delta_T$
    - we are calculating into the future

MPC control horizon prediction horizon
- minimum of 2-3 steps for CH and CH should be 10-20% of PH

Linear MPC, Adaptive MPC, Gain-scheduled MPC, Non-linear MPC, Explicit MPC

---

Summary

- open-loop controllers cannot handle unknown disturbances
- in practice, we therefore require closed-loop control with sensor feedback
- black box don't require knowledge about the process
- most popular black box controller: PID controller 
- geometric controllers exploit geometric relationships for path tracking
- optimal controllers use a vehicle model and optimize a cost function
- MPC (model predictive control) is the most flexible and powerful approach 
- However, MPC requires solving an optimization problem at every step