import carla 

class CarEnv():

    def __init__():
        pass

    def reset():
        pass
    
    def get_state():
        # return x, y, v, psi, beta
        pass

    # TODO: get waypoints

    def step(self, action):
        
        steer, throttle, brake = action

        control = carla.VehicleControl(steer=steer, throttle=throttle, brake=brake)
        self.vehicle.apply_control(control)

        # TODO: create a windows to view and save images

        done = None
        new_state = None
        waypoints = None

        return new_state, waypoints, done