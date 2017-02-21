
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import yaml

# Deliberately terrible code for teaching purposes

config = yaml.load(open("boids/config.yaml"))

boids = range(boid_number)

def initialise(limits, boids):
    values = [random.uniform(limits[0], limits[1]) for x in boids]
    return values

def new_flock():
    x_positions = initialise(x_position_limits, boids)
    y_positions = initialise(y_position_limits, boids)
    x_velocities = initialise(x_velocity_limits, boids)
    y_velocities = initialise(y_velocity_limits, boids)
    boid_positions = (x_positions, y_positions)
    boid_velocities = (x_velocities, y_velocities)
    return boid_positions, boid_velocities

boid_positions, boid_velocities = new_flock()

def proximity(i, j, boid_positions, boid_velocities, distance):
    return (boid_positions[0][j]-boid_positions[0][i])**2 + (boid_positions[1][j]-boid_positions[1][i])**2 < distance

def fly_towards_middle(i, j, boid_positions, boid_velocities):
    boid_velocities[0][i] = boid_velocities[0][i]+(boid_positions[0][j]-boid_positions[0][i])*middle_scaling/boid_number
    boid_velocities[1][i] = boid_velocities[1][i]+(boid_positions[1][j]-boid_positions[1][i])*middle_scaling/boid_number
    
    return boid_positions, boid_velocities

def avoid_boids(i, j, boid_positions, boid_velocities):
    if proximity(i,j,boid_positions,boid_velocities,avoid_distance):
        boid_velocities[0][i] = boid_velocities[0][i]+(boid_positions[0][i]-boid_positions[0][j])
        boid_velocities[1][i] = boid_velocities[1][i]+(boid_positions[1][i]-boid_positions[1][j])
        
    return boid_positions, boid_velocities

def match_speed(i, j, boid_positions, boid_velocities):
    if proximity(i,j,boid_positions,boid_velocities,match_speed_distance):
        boid_velocities[0][i] = boid_velocities[0][i]+(boid_velocities[0][j]-boid_velocities[0][i])*match_scaling/boid_number
        boid_velocities[1][i] = boid_velocities[1][i]+(boid_velocities[1][j]-boid_velocities[1][i])*match_scaling/boid_number
        
    return boid_positions, boid_velocities

def update_boids(boid_positions, boid_velocities):
    for i in boids:
        for j in boids:
            fly_towards_middle(i,j,boid_positions, boid_velocities)
            avoid_boids(i,j,boid_positions, boid_velocities)
            match_speed(i,j,boid_positions, boid_velocities)
                
    # Move according to velocities
    for i in boids:
        boid_positions[0][i] = boid_positions[0][i]+boid_velocities[0][i]
        boid_positions[1][i] = boid_positions[1][i]+boid_velocities[1][i]
        
    return boid_positions, boid_velocities

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500,1500))
scatter = axes.scatter(boid_positions[0], boid_positions[1])

def animate(frame):
    update_boids(boid_positions, boid_velocities)
    x_pos = np.array(boid_positions[0])
    y_pos = np.array(boid_positions[1])
    data = np.hstack((x_pos[:,np.newaxis], y_pos[:, np.newaxis]))
    scatter.set_offsets(data)
    
anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ =="__main__":
    plt.show()