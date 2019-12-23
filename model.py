

from random import shuffle
import operator
import matplotlib.pyplot as plt
from AgentFrameWork import Agent
import sys

try: num_of_agents = int(sys.argv[1])
except: num_of_agents = 10
try: num_of_iteration = int(sys.argv[2])
except: num_of_iteration = 100
try:visual_on = eval(sys.argv[4].title())
except:visual_on = True 

#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.y - agents_row_b.y)**2) +
#        ((agents_row_a.x - agents_row_b.x)**2))**0.5
#num_of_agents = 10
#num_of_iterations = 100
#neighbourhood = 20
#num_of_agents = int(sys.argv[1]) #10
#num_of_iterations = int(sys.argv[2])
#neighbourhood  = int(sys.argv[3]) #20
#visual_on = eval(sys.argv[4].title())
agents = []
environment = []

with open("in.txt") as file: 
    for line in file:
        row = list(eval(line))
        environment.append(row)    
# Make the agents.
for i in range(num_of_agents):
    agents.append(Agent(environment, agents))
# Move the agents.
for j in range(num_of_iterations):
    shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
if visual_on:        
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