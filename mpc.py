import numpy as np
from carla_car_env import *
from ilqr import *
# carla init

env = CarEnv()

for i in range(1):
    state, waypoints = env.reset()

    # total_time = 0

    controller = iLQR()

    for k in 1000:
        # start = time.time()
        
        # TODO: start a random trajectory
        u_trj = None

        state[2] += 0.01
        state = np.array(state)
        
        waypoints = np.array(waypoints)
        
        T = controller.control()
        
        # TODO: prepare the input
        steering = None
        throttle = None
        brake = None

        state, waypoints, done, _ = env.step((steering, throttle, brake))
