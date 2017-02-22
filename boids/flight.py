
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
                boid_positions, boid_velocities = self.fly_towards_middle(i,j,self.boid_positions, self.boid_velocities)
                boid_positions, boid_velocities = self.avoid_boids(i,j,boid_positions, boid_velocities)
                boid_positions, boid_velocities = self.match_speed(i,j,boid_positions, boid_velocities)
                
        for i in boids:
            boid_positions = self.move(boid_positions, boid_velocities, i)
        
        return boid_positions, boid_velocities