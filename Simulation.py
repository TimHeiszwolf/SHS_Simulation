import math
from Container import Container

class Simulation:
	def __init__(self, containers, routing, delta_time, power):
		self.time=0.0
		self.delta_time = delta_time
		self.power = power
		
		self.containers = containers#List with all the containers
		self.routing = routing#Dict with key for container ID and lists of output target (hopefully never more than one)
		
	def run_tick(self):
		"""
		Runs a single tick of the simulation.
		
		>>> sim=Get_Simple_Containers_and_Routing()
		>>> sim.containers[0].volume
		0.15707963267948968
		>>> sim.containers[0].volume_capacity
		1.570796326794897
		>>> sim.containers[1].volume
		0.0
		>>> sim.containers[1].volume_capacity
		3.1415926535897933e-06
		>>> sim.run_tick()
		>>> sim.containers[0].volume
		0.15706763267948967
		>>> sim.containers[1].volume
		3.1415926535897925e-06
		>>> (round(sim.containers[1].volume, 4)==round(sim.containers[2].volume, 4))and(round(sim.containers[1].volume, 4)==round(sim.containers[3].volume, 4))
		True
		>>> sim.containers[4].volume
		2.575222039230623e-06
		>>> sim.containers[5].volume
		0.0
		>>> sim.containers[199].volume
		0.0
		>>> sim.run_amount_of_ticks(200)
		"""
		for current_container in self.containers:
			current_container.conduct_heat(self.delta_time, self.power)
			output = current_container.volume_Output(self.delta_time)
			
			output_container_ID = self.routing[str(current_container.ID)][0]#This means it currently only works for one output container
			
			for output_container in self.containers:
				if output_container.ID == output_container_ID:
					output_container.volume_Input(output, self.delta_time)
					break
		
		self.time = self.time+self.delta_time
	
	def run_amount_of_ticks(self, amount):
		"""
		"""
		for i in range(amount):
			self.run_tick()

	

def Get_Simple_Containers_and_Routing():
	containers=[]
	
	containers.append(Container(0, 0.5*(2**0.5), 1, 0.0025, 10, 293, 12*(10**-5)))#Huge container with pump
	
	for i in range(200):
		containers.append(Container(1+i, 0.01, 0.01, 0.0025, 0, 293, 0))
	
	Routing={}
	
	for i in range(200):
		Routing[str(i)]=[i+1]
	
	Routing['200']=[0]
	
	return Simulation(containers, Routing, 0.1, 1000)

if __name__ == "__main__":
    import doctest
    doctest.testmod()