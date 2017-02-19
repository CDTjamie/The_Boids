
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

# Deliberately terrible code for teaching purposes

boid_count = range(50)

def new_flock():
    boids_x = [random.uniform(-450, 50.0) for x in boid_count]
    boids_y = [random.uniform(300.0, 600.0) for x in boid_count]
    boid_x_velocities = [random.uniform(0, 10.0) for x in boid_count]
    boid_y_velocities = [random.uniform(-20.0, 20.0) for x in boid_count]
    boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)
    return boids

boids = new_flock()

def fly_towards_middle(i, j, xs, ys, xvs, yvs):
    xvs[i] = xvs[i]+(xs[j]-xs[i])*(0.01/len(xs))
    yvs[i] = yvs[i]+(ys[j]-ys[i])*(0.01/len(xs))
    
    return xvs[i], yvs[j]

def avoid_boids(i, j, xs, ys, xvs, yvs):
    if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
        xvs[i] = xvs[i]+(xs[i]-xs[j])
        yvs[i] = yvs[i]+(ys[i]-ys[j])
        
    return xvs[i], yvs[i]

def match_speed(i, j, xs, ys, xvs, yvs):
    if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 <10000:
        xvs[i] = xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
        yvs[i] = yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
        
    return xvs[i], yvs[i]

def update_boids(boids):
    xs, ys, xvs, yvs = boids
    
    for i in boid_count:
        for j in boid_count:
            fly_towards_middle(i,j,xs,ys,xvs,yvs)
            avoid_boids(i,j,xs,ys,xvs,yvs)
            match_speed(i,j,xs,ys,xvs,yvs)
                
    # Move according to velocities
    for i in boid_count:
        xs[i] = xs[i]+xvs[i]
        ys[i] = ys[i]+yvs[i]

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