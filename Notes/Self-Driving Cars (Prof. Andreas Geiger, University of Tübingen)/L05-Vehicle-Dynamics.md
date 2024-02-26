# Vehicle Dynamics

mapping directly from images to the vehicle control is possible, as we have seen previously, but it is not the most efficient approach

in practice it is often better to have a separate controller 


kinematic

kinetic 

holonomic constrains

- constrain on the configuration space
- particle that moves in 3d space and is constrained to 2d motion
- but the system can move freely in that space
- controllable degrees of freedom is equal to the degrees of freedom

non-holonomic constrains

- constrains on the velocity
- assume a vehicle that is parametrized by $(x, y, \psi) \in \mathbb{R} \times [0, 2\pi]$
- $\psi$ heading direction of the vehicle wrt to coordinate system
- the 2D vehicle velocity is given by 
    - $\dot x = v \cos{\psi}$
    - $\dot y = v \sin{\psi}$
    - $\dot x \sin{\psi} - \dot y \cos{\psi} = 0$
- the car cannot move freely in any direction 

Coordinate system

- Inertial frame: fixed to earth with vertical Z-axis and X/Y horizontal plane
- Vehicle frame: attached to vehicle at fixed reference point; $x_v$ points forward, $y_v$ to the side and $z_v$ to the top of the vehicle 
- Horizontal frame: original at vehicle reference point (like vehicle frame) but x and y axes are projections of $x_{v^-}$ and $y_{v^-}$ axes onto the X/Y horizontal plane

kinematics of a point

kinematics of a rigid body

instantaneous center of rotation

## Kinematic bicycle model 

a simple model under the assumption that wheels do not slip 

assumptions

- the vehicle moves according to some rotation center with turning radius $R$
    - $R$ is set on the intersection of norms (orthogonal lines) of $v_r$ and $v_f$ 
    - it is called ICC (instantaneous center of curvature)
- planar motion (no roll, no pitch, only heading $\psi$)
    - the direction that the vehicle is heading wrt inertial frame
- low speed => no wheel splip (wheel orientation = wheel velocity)
    - $v_r$ and $v_f$ rear and from wheel velocity
    - $\delta_r$ and $\delta_f$ rear and front streering angle
- wheelbase $L = l_r + l_f$
    - $l_r$ distance from the rear wheel to the center of gravity $C$
    - $l_f$ distance from the front wheel to the center of gravity $C$
- course angle $\psi + \beta$
    - $\psi$ heading angle 
    - $\beta$ slip angle. ortogonal to the turning radius of the rotation center
    - the direction of vehicle velocity $v$

motion equations:

- $\dot X = v \cos{(\psi + \beta)}$
- $\dot Y = v \sin{(\psi + \beta)}$
- (steering front)
    - $\dot \psi = \dfrac{v \cos{(\beta)}}{l_f+l_r} \tan (\delta_f)$ 
    - $\dot \beta = \tan^{-1}\left(\dfrac{l_r \tan(\delta_f)}{l_f+l_r}\right)$
    - $\tan (\delta) = \dfrac{l_f + l_r}{R'}$
        - $R'$ distance of the rotation center to the rear wheel
    - $\tan (\beta) = \dfrac{l_r}{R'}$
- (steering front and rear)
    - $\dot \psi = \dfrac{v \cos{(\beta)}}{l_f+l_r} (\tan (\delta_f) - \tan (\delta_r))$
    - $\dot \beta = \tan^{-1}\left(\dfrac{l_f \tan (\delta_r) + l_r \tan(\delta_f)}{l_f+l_r}\right)$

time discretized model (assuming that $\delta$ and $\beta$ are small)

- $X_{t+1} = x_t + v\cos(\psi)\Delta t$
- $Y_{t+1} = y_t + v\sin(\psi)\Delta t$
- $\psi_{t+1} = \psi_t + \dfrac{v\delta}{l_f+l_r}\Delta t$

Ackermann Steering Geometry

- in practice the left and right wheel streering angles are not equal if no wheel slip
- if angles are small, the left/right streering wheel angles can be approximated
    - $\delta_l \approx \tan\left(\dfrac{L}{R + 0.5B}\right) \approx \dfrac{L}{R + 0.5B}$
    - $\delta_r \approx \tan\left(\dfrac{L}{R - 0.5B}\right) \approx \dfrac{L}{R - 0.5B}$
    - where track $B$ is the distance between the two rear wheels 

## Tire models

tread block model

circle of forces

- forces in X and Y direction are dependent. If the net force is exceeding some limit, then the vehicle will slip

## Dynamic bicycle model

car model has 6 degrees of freedom 

rotatory motion of a rigid body 

assumptions

lateral dynamics

yaw dynamics

tire forces

state space representation

state x:
- $v_y$ lateral velocity
- $\psi$ heading velocity
- $\omega$ angular velocity


$c_r$ cornering stiffness factor for the rear wheel

$\alpha_r$ rear wheel slip angle