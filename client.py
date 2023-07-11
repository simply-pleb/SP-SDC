from time import sleep
import numpy as np

import cv2

import carla

import sys
sys.path.append('C:\Games\Carla\PythonAPI\carla') # tweak to where you put carla
from agents.navigation.global_route_planner import GlobalRoutePlanner


def initialize_car(client) -> carla.Vehicle:
    #define environment/world and get possible places to spawn a car
    # start a car
    world = client.get_world()
    spawn_points = world.get_map().get_spawn_points()
    #look for a blueprint of Mini car
    vehicle_bp = world.get_blueprint_library().filter('*Cybertruck*')

    start_point = spawn_points[0]
    vehicle = world.try_spawn_actor(vehicle_bp[0], start_point)
    
    # TODO: return car location
    return vehicle, start_point

def initialize_camera(client, vehicle):
    #setting RGB Camera - this follow the approach explained in a Carla video
    # link: https://www.youtube.com/watch?v=om8klsBj4rc&t=1184s

    #camera mount offset on the car - you can tweak these to have the car in view or not
    CAMERA_POS_Z = 3 
    CAMERA_POS_X = -5 

    world = client.get_world()

    camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')
    camera_bp.set_attribute('image_size_x', '640') # this ratio works in CARLA 9.14 on Windows
    camera_bp.set_attribute('image_size_y', '360')

    camera_init_trans = carla.Transform(carla.Location(z=CAMERA_POS_Z,x=CAMERA_POS_X))
    #this creates the camera in the sim
    camera = world.spawn_actor(camera_bp,camera_init_trans,attach_to=vehicle)

    def camera_callback(image,data_dict):
        data_dict['image'] = np.reshape(np.copy(image.raw_data),(image.height,image.width,4))

    image_w = camera_bp.get_attribute('image_size_x').as_int()
    image_h = camera_bp.get_attribute('image_size_y').as_int()

    camera_data = {'image': np.zeros((image_h,image_w,4))}
    # this actually opens a live stream from the camera
    camera.listen(lambda image: camera_callback(image,camera_data))

    return camera

def get_route_and_plot(client, start_point):

    world = client.get_world()
    spawn_points = world.get_map().get_spawn_points()

    # create and show the navigation route like in Tutorial 3
    point_a = start_point.location #we start at where the car is
    sampling_resolution = 1
    grp = GlobalRoutePlanner(world.get_map(), sampling_resolution)
    # now let' pick the longest possible route
    distance = 0
    for loc in spawn_points: # we start trying all spawn points 
                                #but we just exclude first at zero index
        cur_route = grp.trace_route(point_a, loc.location)
        if len(cur_route)>distance:
            distance = len(cur_route)
            route = cur_route
    #draw the route in sim window - Note it does not get into the camera of the car
    for waypoint in route:
        world.debug.draw_string(waypoint[0].transform.location, '^', draw_shadow=False,
            color=carla.Color(r=0, g=0, b=255), life_time=30.0,
            persistent_lines=True)
    
    return route

def destroy_setup(client, camera):
    # clean after utility
    cv2.destroyAllWindows()
    
    world = client.get_world()
    
    camera.stop() # this is the opposite of camera.listen
    for actor in world.get_actors().filter('*vehicle*'):
        actor.destroy()
    for sensor in world.get_actors().filter('*sensor*'):
        sensor.destroy()

def run_episode(client : carla.Client, vehicle, controller, waypoints, frames_per_episode=1000): # TODO: add the rest of the parameters
    cur_closest_waypoint = None
    prev_closest_waypoint = None
    waypoints_num = waypoints.shape[0]

    for frame in range(frames_per_episode):
        # TODO: read https://carla.readthedocs.io/en/0.9.5/measurements/
        measurements, sensor_data = client.read_data()

        control_traj = controller.control(waypoints, measurements)

        # TODO: chech if we made a whole lap. but is this necessery? 

        steer, throttle, brake = control_traj['steer'], control_traj['throttle'], control_traj['brake']
        
        # TODO: add steer and throttle noise
        
        control = carla.VehicleControl(steer=steer, throttle=throttle, brake=brake)

        # TODO: send control to client
        vehicle.apply_control(control)
    pass

def run_carla_client():
    # connect to carla server
    client = carla.Client('localhost', 2000)
    episode_num = 0
    fails_num = 0
    try:
        while episode_num < 1: # TODO: add number of episodes arg
            vehicle, start_point = initialize_car(client)
            camera = initialize_camera(client, vehicle)
            route = get_route_and_plot(client, start_point)
            # TODO: initialize controller
            controller = None
            # TODO: get upcomming waypoints, not all waypoints in route
            # waypoints = None

            # run_episode(client, controller, route, 10000) # TODO: add frames per episode parameter
            control = carla.VehicleControl(throttle=1, steer=0)
            vehicle.apply_control(control)
            sleep(5)
            control = carla.VehicleControl(brake=1, steer=1)
            vehicle.apply_control(control)
            sleep(5)

            destroy_setup(client, camera)

            episode_num += 1
    except KeyboardInterrupt:
        destroy_setup(client, camera)
        print('\nKeyboard interrupt.')

def main():
    run_carla_client()

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('\nKeyboard interrupt.')
