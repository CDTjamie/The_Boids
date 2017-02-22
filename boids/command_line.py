#!/usr/bin/env python
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import yaml
from boids.flock import Flock
from flight import Flight

config = yaml.load(open("config.yaml"))
boid_number = config["boid_number"]
x_position_limits = config["x_position_limits"]
y_position_limits = config["y_position_limits"]
x_velocity_limits = config["x_velocity_limits"]
y_velocity_limits = config["y_velocity_limits"]
avoid_distance = config["avoid_distance"]
match_speed_distance = config["match_speed_distance"]
middle_scaling = config["middle_scaling"]
match_scaling = config["match_scaling"]



def process(boid_number, x_position_limits, y_position_limits, x_velocity_limits, y_velocity_limits, avoid_distance, match_speed_distance, middle_scaling, match_scaling):
    myflock = Flock(boid_number, x_position_limits, y_position_limits, x_velocity_limits, y_velocity_limits)
    boid_positions, boid_velocities = myflock.new_flock()

    figure = plt.figure()
    axes = plt.axes(xlim=(-500, 1500), ylim=(-500,1500))
    scatter = axes.scatter(boid_positions[0], boid_positions[1])
    
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
        
    anim
    
if __name__ == "__main__":
    process(boid_number, x_position_limits, y_position_limits, x_velocity_limits, y_velocity_limits, avoid_distance, match_speed_distance, middle_scaling, match_scaling)