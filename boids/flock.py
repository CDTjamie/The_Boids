
import random

class Flock(object):
    def __init__(self, boid_number, x_position_limits, y_position_limits, x_velocity_limits, y_velocity_limits):
        self.boid_number = boid_number
        self.x_position_limits = x_position_limits
        self.y_position_limits = y_position_limits
        self.x_velocity_limits = x_velocity_limits
        self.y_velocity_limits = y_velocity_limits
        
    def initialise(self, limits, boids):
        values = [random.uniform(limits[0], limits[1]) for x in boids]
        return values
    
    def new_flock(self):
        boids = range(self.boid_number)
        x_positions = self.initialise(self.x_position_limits, boids)
        y_positions = self.initialise(self.y_position_limits, boids)
        x_velocities = self.initialise(self.x_velocity_limits, boids)
        y_velocities = self.initialise(self.y_velocity_limits, boids)
        boid_positions = (x_positions, y_positions)
        boid_velocities = (x_velocities, y_velocities)
        return boid_positions, boid_velocities