
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

# Deliberately terrible code for teaching purposes

boid_count = range(50)

def initialise(lower_limit, upper_limit, boid_count):
    values = [random.uniform(lower_limit, upper_limit) for x in boid_count]
    return values

def new_flock():
    x_positions = initialise(-450, 50.0, boid_count)
    y_positions = initialise(300.0, 600.0, boid_count)
    x_velocities = initialise(0, 10.0, boid_count)
    y_velocities = initialise(-20.0, 20.0, boid_count)
    boid_positions = (x_positions, y_positions)
    boid_velocities = (x_velocities, y_velocities)
    return boid_positions, boid_velocities

boid_positions, boid_velocities = new_flock()

def proximity(i, j, boid_positions, boid_velocities, distance):
    return (boid_positions[0][j]-boid_positions[0][i])**2 + (boid_positions[1][j]-boid_positions[1][i])**2 < distance

def fly_towards_middle(i, j, boid_positions, boid_velocities):
    boid_velocities[0][i] = boid_velocities[0][i]+(boid_positions[0][j]-boid_positions[0][i])*0.01/50
    boid_velocities[1][i] = boid_velocities[1][i]+(boid_positions[1][j]-boid_positions[1][i])*0.01/50
    
    return boid_positions, boid_velocities

def avoid_boids(i, j, boid_positions, boid_velocities):
    if proximity(i,j,boid_positions,boid_velocities,100):
        boid_velocities[0][i] = boid_velocities[0][i]+(boid_positions[0][i]-boid_positions[0][j])
        boid_velocities[1][i] = boid_velocities[1][i]+(boid_positions[1][i]-boid_positions[1][j])
        
    return boid_positions, boid_velocities

def match_speed(i, j, boid_positions, boid_velocities):
    if proximity(i,j,boid_positions,boid_velocities,10000):
        boid_velocities[0][i] = boid_velocities[0][i]+(boid_velocities[0][j]-boid_velocities[0][i])*0.125/50
        boid_velocities[1][i] = boid_velocities[1][i]+(boid_velocities[1][j]-boid_velocities[1][i])*0.125/50
        
    return boid_positions, boid_velocities

def update_boids(boid_positions, boid_velocities):
    for i in boid_count:
        for j in boid_count:
            fly_towards_middle(i,j,boid_positions, boid_velocities)
            avoid_boids(i,j,boid_positions, boid_velocities)
            match_speed(i,j,boid_positions, boid_velocities)
                
    # Move according to velocities
    for i in boid_count:
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