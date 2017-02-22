
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import yaml

# Deliberately terrible code for teaching purposes

config = yaml.load(open("boids/config.yaml"))
boid_number = config["boid_number"]
x_position_limits = config["x_position_limits"]
y_position_limits = config["y_position_limits"]
x_velocity_limits = config["x_velocity_limits"]
y_velocity_limits = config["y_velocity_limits"]
avoid_distance = config["avoid_distance"]
match_speed_distance = config["match_speed_distance"]
middle_scaling = config["middle_scaling"]
match_scaling = config["match_scaling"]

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

myflock = Flock(boid_number, x_position_limits, y_position_limits, x_velocity_limits, y_velocity_limits)
boid_positions, boid_velocities = myflock.new_flock()

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500,1500))
scatter = axes.scatter(boid_positions[0], boid_positions[1])


class Flight(object):
    def __init__(self, boid_number, boid_positions, boid_velocities, avoid_distance, match_speed_distance, middle_scaling, match_scaling):
        self.boid_number = boid_number
        self.boid_positions = boid_positions
        self.boid_velocities = boid_velocities
        self.avoid_distance = avoid_distance
        self.match_speed_distance = match_speed_distance
        self.middle_scaling = middle_scaling
        self.match_scaling = match_scaling
        
    def proximity(self, i, j, boid_positions, boid_velocities, distance):
        return (boid_positions[0][j]-boid_positions[0][i])**2 + (boid_positions[1][j]-boid_positions[1][i])**2 < distance
    
    def fly_towards_middle(self, i, j, boid_positions, boid_velocities):
        boid_velocities[0][i] = boid_velocities[0][i]+(boid_positions[0][j]-boid_positions[0][i])*self.middle_scaling/self.boid_number
        boid_velocities[1][i] = boid_velocities[1][i]+(boid_positions[1][j]-boid_positions[1][i])*self.middle_scaling/self.boid_number
    
        return boid_positions, boid_velocities
        
    def avoid_boids(self, i, j, boid_positions, boid_velocities):
        if self.proximity(i,j,boid_positions,boid_velocities,self.avoid_distance):
            boid_velocities[0][i] = boid_velocities[0][i]+(boid_positions[0][i]-boid_positions[0][j])
            boid_velocities[1][i] = boid_velocities[1][i]+(boid_positions[1][i]-boid_positions[1][j])
        
        return boid_positions, boid_velocities
    
    def match_speed(self, i, j, boid_positions, boid_velocities):
        if self.proximity(i,j,boid_positions,boid_velocities,self.match_speed_distance):
            boid_velocities[0][i] = boid_velocities[0][i]+(boid_velocities[0][j]-boid_velocities[0][i])*self.match_scaling/self.boid_number
            boid_velocities[1][i] = boid_velocities[1][i]+(boid_velocities[1][j]-boid_velocities[1][i])*self.match_scaling/self.boid_number
        
        return boid_positions, boid_velocities
    
    def move(self, boid_positions, boid_velocities, i):
        boid_positions[0][i] = boid_positions[0][i]+boid_velocities[0][i]
        boid_positions[1][i] = boid_positions[1][i]+boid_velocities[1][i]
    
        return boid_positions
    
    def update_boids(self):
        boids = range(self.boid_number)
    
        for i in boids:
            for j in boids:
                self.fly_towards_middle(i,j,self.boid_positions, self.boid_velocities)
                self.avoid_boids(i,j,self.boid_positions, self.boid_velocities)
                self.match_speed(i,j,self.boid_positions, self.boid_velocities)
                
        for i in boids:
            boid_positions = self.move(self.boid_positions, self.boid_velocities, i)
        
        return boid_positions, boid_velocities

myflight = Flight(boid_number, boid_positions, boid_velocities, avoid_distance, match_speed_distance, middle_scaling, match_scaling)

def animate(frame):
    boid_positions, boid_velocities = myflight.update_boids()
    x_pos = np.array(boid_positions[0])
    y_pos = np.array(boid_positions[1])
    data = np.hstack((x_pos[:,np.newaxis], y_pos[:, np.newaxis]))
    scatter.set_offsets(data)
    
anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ =="__main__":
    plt.show()