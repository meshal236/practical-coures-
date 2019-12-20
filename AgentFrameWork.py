

""

from random import randint , random 

class Agent: 
    
    def __init__(self):
        self.x = randint (0,99)
        self.y = randint (0,99)
    def move(self):
       
        if random() < 0.5:
            self.y = ( self.y + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.x = (self.x - 1) % 100
