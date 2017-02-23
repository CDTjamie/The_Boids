
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