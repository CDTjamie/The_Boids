
from nose.tools import assert_raises, assert_equal
from boids.flock import Flock
import yaml
import os

def test_init():
    _ROOT = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(_ROOT,'config_wrong1.yaml')) as config_file:
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
    
    with assert_raises(TypeError) as exception: Flock(boid_number, x_position_limits, y_position_limits, x_velocity_limits, y_velocity_limits)

    _ROOT = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(_ROOT,'config_wrong2.yaml')) as config_file:
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
    
    with assert_raises(ValueError) as exception: Flock(boid_number, x_position_limits, y_position_limits, x_velocity_limits, y_velocity_limits)
        
    _ROOT = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(_ROOT,'config_wrong3.yaml')) as config_file:
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
    
    with assert_raises(ValueError) as exception: Flock(boid_number, x_position_limits, y_position_limits, x_velocity_limits, y_velocity_limits)
        
def test_random():
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
    values = temp_flock.initialise(x_position_limits, range(boid_number))
    
    assert type(values) == list
    assert type(values[0]) == float
    
def test_new_flock():
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
    
    assert type(boid_positions) == tuple
    assert type(boid_velocities) == tuple
    assert type(boid_positions[0][0]) == float
    assert type(boid_positions[1][0]) == float
    assert type(boid_velocities[0][0]) == float
    assert type(boid_velocities[1][0]) == float