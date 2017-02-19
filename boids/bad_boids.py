
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

# Deliberately terrible code for teaching purposes

boid_count = range(50)

def new_flock():
    x_positions = [random.uniform(-450, 50.0) for x in boid_count]
    y_positions = [random.uniform(300.0, 600.0) for x in boid_count]
    x_velocities = [random.uniform(0, 10.0) for x in boid_count]
    y_velocities = [random.uniform(-20.0, 20.0) for x in boid_count]
    initial_boids = (x_positions, y_positions, x_velocities, y_velocities)
    return initial_boids

boids = new_flock()

def proximity(i, j, boids, distance):
    return (boids[0][j]-boids[0][i])**2 + (boids[1][j]-boids[1][i])**2 < distance

def fly_towards_middle(i, j, boids):
    boids[2][i] = boids[2][i]+(boids[0][j]-boids[0][i])*0.01/50
    boids[3][i] = boids[3][i]+(boids[1][j]-boids[1][i])*0.01/50
    
    return boids

def avoid_boids(i, j, boids):
    if proximity(i,j,boids,100):
        boids[2][i] = boids[2][i]+(boids[0][i]-boids[0][j])
        boids[3][i] = boids[3][i]+(boids[1][i]-boids[1][j])
        
    return boids

def match_speed(i, j, boids):
    if proximity(i,j,boids,10000):
        boids[2][i] = boids[2][i]+(boids[2][j]-boids[2][i])*0.125/50
        boids[3][i] = boids[3][i]+(boids[3][j]-boids[3][i])*0.125/50
        
    return boids

def update_boids(boids):
    for i in boid_count:
        for j in boid_count:
            fly_towards_middle(i,j,boids)
            avoid_boids(i,j,boids)
            match_speed(i,j,boids)
                
    # Move according to velocities
    for i in boid_count:
        boids[0][i] = boids[0][i]+boids[2][i]
        boids[1][i] = boids[1][i]+boids[3][i]

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500,1500))
scatter = axes.scatter(boids[0], boids[1])

def animate(frame):
    update_boids(boids)
    x_pos = np.array(boids[0])
    y_pos = np.array(boids[1])
    data = np.hstack((x_pos[:,np.newaxis], y_pos[:, np.newaxis]))
    scatter.set_offsets(data)
    
anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ =="__main__":
    plt.show()