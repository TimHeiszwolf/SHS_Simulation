import math
import Container

class Simulation:
	def __init__(self, containers, routing, delta_time):
		self.time=0.0
		self.delta_time = delta_time
		
		self.containers = containers#List with all the containers
		self.routing = routing#Dict with key for container ID and lists of output target (hopefully never more than one)
		
	def run_tick(self):
		for current_container in self.containers:
			current_container.conduct_heat(self.delta_time, 0)
			output = current_container.volume_Output(self.delta_time)
			
			output_container_ID = self.routing[str(current_container.ID)][0]#This means it currently only works for one output container
			
			for output_container in self.container:
				if output_container.ID == output_container_ID:
					output_container.volume_Input(output, self.delta_time)
					break

	

def Get_Simple_Containers_and_Routing():
	containers=[]
	
	containers.append(container(0, 0.5*(2**0.5), 1, 10, 293, 3*(10**-9)))#Huge container with pump
	
	for i in range(200):
		containers.append(container(1+i,0.01,0.01, 0, 293, 0))
	
	Routing={}
	
	for i in range(200):
		rounting[str(i)]=[i+1]
	
	rounting['200']=[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()