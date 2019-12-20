



from random import randint , random 

class Agent: 
    
    def __init__(self, environment):
        self.x = randint (0, len(environment) -1)
        self.y = randint (0, len(environment) -1)
        self.environment = environment
        self.store = 0 
        
    def move(self):
        if random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)

        if random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.y] -= 10
            self.store +=10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0 
    def __str__(self):
        return f"x: {self.x}, y:{self.y}, store:{self.store}"
    