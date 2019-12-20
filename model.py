


import random
import operator
import matplotlib.pyplot as plt
from AgentFrameWork import Agent

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.y - agents_row_b.y)**2) +
        ((agents_row_a.x - agents_row_b.x)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []
environment = []

with open("in.txt") as file: 
    for line in file:
        row = list(eval(line))
        environment.append(row)
    
# Make the agents.
for i in range(num_of_agents):
    agents.append(Agent(environment))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
plt.xlim(0, len(environment) -1)
plt.ylim(0, len(environment) -1)
for i in range(num_of_agents):
    plt.scatter(agents[i].y,agents[i].x)
plt.imshow(environment)
plt.show()

#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b)
#        print (distance)
        
with open("out.txt","w") as file:
    for row in environment:
        for value in row:
            file.write(f"{value},")
        file.write("\n")
with open("stores.txt","a") as file :
    for agent in agents :
        file.write(f"{agent.store},")
    file.write("\n")
    

