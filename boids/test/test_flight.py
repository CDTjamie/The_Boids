
from nose.tools import assert_raises, assert_equal
from boids.flock import Flock
from boids.flight import Flight
import yaml
import os

def test_init():
    _ROOT = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(_ROOT,'config_correct.yaml')) as config_file:
        config = yaml.load(config_file)
        
    boid_number = config["boid_number"]
    x_position_limits = config["x_position_limits"]
    y_position_limits = config["y_position_limits"]
    x_velocity_limits = config["x_velocity_limits"]
    y_velocity_limits = config["y_velocity_limits"]
    avoid_distance = config["avoid_distance"]
    match_speed_distance = config["match_speed_distance"]
    middle_scaling = config["middle_scaling"]
    match_scaling = config["match_scaling"]
    
    boid_positions = 50.0
    boid_velocities = "velocity"
    
    with assert_raises(TypeError) as exception: Flight(boid_number, ([5.,5.],[5.,5.]), boid_velocities, avoid_distance, match_speed_distance, middle_scaling, match_scaling)
    with assert_raises(TypeError) as exception: Flight(boid_number, boid_positions, ([5.,5.],[5.,5.]), avoid_distance, match_speed_distance, middle_scaling, match_scaling)
        
def test_update_boids():
    _ROOT = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(_ROOT,'config_correct.yaml')) as config_file:
        config = yaml.load(config_file)
        
    boid_number = config["boid_number"]
    x_position_limits = config["x_position_limits"]
    y_position_limits = config["y_position_limits"]
    x_velocity_limits = config["x_velocity_limits"]
    y_velocity_limits = config["y_velocity_limits"]
    avoid_distance = config["avoid_distance"]
    match_speed_distance = config["match_speed_distance"]
    middle_scaling = config["middle_scaling"]
    match_scaling = config["match_scaling"]
    
    temp_flock = Flock(boid_number, x_position_limits, y_position_limits, x_velocity_limits, y_velocity_limits)
    boid_positions, boid_velocities = temp_flock.new_flock()
    temp_flight = Flight(boid_number, boid_positions, boid_velocities, avoid_distance, match_speed_distance, middle_scaling, match_scaling)
    
    boid_positions, boid_velocities = temp_flight.update_boids()
    
    assert type(boid_positions) == tuple
    assert type(boid_velocities) == tuple
    assert type(boid_positions[0][0]) == float
    assert type(boid_positions[1][0]) == float
    assert type(boid_velocities[0][0]) == float
    assert type(boid_velocities[1][0]) == float