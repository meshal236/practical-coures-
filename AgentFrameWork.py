
from random import randint , random 
class Agent: 
    def __init__(self, environment,agents, y, x):
        self.x = x
        self.y = y 
        self.environment = environment
        self.store = 0 
        self.agents = agents
        
    def move(self):
        if random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.y = (self.y - 1) % len(self.environment)

        if random() < 0.5:
            self.x = (self.x + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 4 
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        
#        if self.store > 100:
#            self.environment[self.y][self.x] += self.store
#            self.store = 0 
    def __str__(self):
        return f"x: {self.x}, y:{self.y}, store:{self.store}"    
    def share_with_neighbours (self,neighbourhood):
        for agent in self.agents:
            score = self.distance_between(agent)
            if score <= neighbourhood:
                average_store = (self.store + agent.store) /2
                self.store = average_store
                agent.store = average_store
#                print("sharing " + str(score) + " " + str(average_store))
              
    def distance_between(self, agent):
        return ((self.y - agent.y)**2 +(self.x - agent.x)**2)**0.5    