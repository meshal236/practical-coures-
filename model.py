

import matplotlib 
matplotlib.use('TkAgg')
from random import shuffle
import matplotlib.pyplot as plt
from AgentFrameWork import Agent
import sys
import tkinter
import requests
import bs4

from matplotlib.animation import FuncAnimation 

try: num_of_agents = int(sys.argv[1])
except: num_of_agents = 10
try: num_of_iteration = int(sys.argv[2])
except: num_of_iteration = 100
try : neighbourhood = int(sys.argv[3])
except: neighbourhood = 20 
#try:visual_on = eval(sys.argv[4].title())
#except:visual_on = True 

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

fig = plt.figure()
carry_on = True 

def update(frame_qty):
    global carry_on
    
    fig.clear()
    # Move the agents.
    for j in range(num_of_iteration):
        shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            # print(agents[i])
    for i in range(num_of_agents):
        plt.scatter(agents[i].x,agents[i].y)
    plt.imshow(environment)
    for agent in agents:
        if agent.store <6000:
            return
        
        carry_on = False 
        
def gen_function():
    while carry_on:
        yield 1 
        
    with open("out.txt","w") as file:
        for row in environment:
            for value in row:
                file.write(f"{value},")
        file.write("\n")
    
    with open("stores.txt","a") as file :
        for agent in agents :
            file.write(f"{agent.store},")
        file.write("\n")
        
with open("in.txt") as file: 
    for line in file:
        row = list(eval(line))
        environment.append(row) 
        
def run():
    animation = FuncAnimation (fig, update , frames= gen_function,  repeat=False)
    canvas.draw()

def load_data_from_web():
    r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
# Make the agents.
    for i in range(num_of_agents):
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        agents.append(Agent(environment, agents, y, x))
        
#plt.xlim(0, len(environment) -1)
#plt.ylim(0, len(environment) -1)
#plt.show()
#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b)
#        print (distance)


    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run Model", command=run)

load_data_from_web()


tkinter.mainloop()
