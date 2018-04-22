import math

class Container:
	def __init__(self, ID, radius, length, volume_percentage, temperature, pump):
		self.density = 997.0#Kilogram per cubic meter
		self.heat_capacity = 4185.5#Joule per kilogram kelvin
		self.heat_capacity_container = 1170.0#Joule per kilogram kelvin
		self.pump = float(pump)#Cubic meters per second
		
		
		self.ID = int(ID)
		self.area_container = float(math.pi*2*radius*height)#Square meter
		self.mass_container = float(1400*self.area_container*0.0025)#Kilogram
		self.volume_capacity = float(length*(math.pi*(radius**2)))#Cubic meter
		self.volume = float(self.volume_capacity*volume_percentage/100)#Cubic meter
		self.temperature = float(temperature)#Kelvin
		self.temperature_container = float(temperature)#Kelvin
		
	def mass(self):
		"""
		Calculates the mass of the volume of the mass in the container.
		
		
		"""
		return self.volume*self.density
	
	def conduct_heat(self, delta_time, external_power):
		"""
		For one unit of delta time this adjusts the temperature of the container and water in the container.
		
		
		"""
		self.temperature_container = self.temperature_container+external_power*delta_time/(self.heat_capacity_container*self.mass_container)#https://en.wikipedia.org/wiki/Heat_capacity
		
		internal_power = 0.591*(self.temperature_container-self.temperature)/0.01#No idea of this is right. Mainly the devides by its length bit. https://en.wikipedia.org/wiki/Thermal_conduction#Fourier's_law
		
		self.temperature = self.temperature+internal_power*delta_time/(self.heat_capacity*self.mass())
		
	def volume_Input(self, input_liquid, delta_time):
		"""
		Handels the input and output of liquids of the tube.
		
		
		"""
		input_volume = float(input_liquid['volume'])
		input_temperature = float(input_liquid['temperature'])
		input_heat_capacity = float(input_liquid['heat capacity'])
		input_density = float(input_liquid['density'])
		
		old_mass = self.mass()
		old_temp = self.temperature
		old_volume = self.volume
		
		total_energy = old_mass*old_temp*self.heat_capacity+input_density*input_volume*input_temperature*input_heat_capacity
		
		self.heat_capacity = (old_mass*self.heat_capacity+input_volume*input_density*input_heat_capacity)/(old_mass+input_density*input_mass)#Don't know if right but weighted average of heat capcity by mass
		self.density = (old_mass+input_volume*input_density)/(old_volume+input_volume)
		self.volume = old_volume+input_volume
		self.temperature = total_energy/(self.heat_capacity*self.mass())
	
	def volume_Output(self, input_liquid, delta_time):
		
		output_liquid = {'volume':self.pump*delta_time+max([self.volume-self.volume_capacity, 0.0]), 'temperature': self.temperature, 'heat capacity': self.heat_capacity, 'density': self.density}
		
		self.volume = self.volume-output_liquid['volume']
		
		return output_liquid



def Get_Test_Containers():
	"""
	Gets containers for testing.
	
	>>> Get_Test_Containers()[0].ID
	0
	
	>>> Get_Test_Containers()[2].ID
	2
	"""
	list = []
	
	list.append(Container(0, 0.01, 0.01, 100, 293, 0))#Normal
	list.append(Container(1, 0.01, 0.02, 75, 293*1.25, 0))#Nearly full and quite hot
	list.append(Container(2, 0.03, 0.01, 10, 293, 0))#Nearly empty
	list.append(Container(3, 0.02, 0.02, 1000, 293, 0))#Overfull
	
	return list
	
	

if __name__ == "__main__":
    import doctest
    doctest.testmod()