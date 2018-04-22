import math

class Container:
	def __init__(self, ID, radius, length, depth, volume_percentage, temperature, pump):
		self.density = 997.0#Kilogram per cubic meter
		self.density_container = 1400.0
		self.heat_capacity = 4185.5#Joule per kilogram kelvin
		self.heat_capacity_container = 1170.0#Joule per kilogram kelvin
		self.pump = float(pump)#Cubic meters per second
		
		
		self.radius = radius
		self.length = length
		self.depth = depth
		self.ID = int(ID)
		self.area_container = float(math.pi*2*radius*length)#Square meter
		self.mass_container = float(self.density_container*self.area_container*depth)#Kilogram
		self.volume_capacity = float(length*(math.pi*(radius**2)))#Cubic meter
		self.volume = float(self.volume_capacity*volume_percentage/100)#Cubic meter
		self.temperature = float(temperature)#Kelvin
		self.temperature_container = float(temperature)#Kelvin
		
	def mass(self):
		"""
		Calculates the mass of the volume of the mass in the container.
		
		>>> containers = Get_Test_Containers()
		>>> containers[0].mass()
		0.0031321678756290237
		>>> containers[1].mass()
		0.004698251813443536
		>>> containers[2].mass()
		0.0028189510880661213
		>>> containers[3].mass()
		0.25057343005032195
		
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
		
		>>> containers=Get_Test_Containers()
		>>> containers[0].volume_Input({'volume': 0.0000015, 'temperature': 393.0, 'heat capacity': 3185.5, 'density': 697.0}, 0.5)
		>>> containers[0].volume
		4.641592653589793e-06
		>>> containers[0].temperature
		313.2579935448551
		>>> containers[0].density
		900.0505187369314
		>>> containers[0].heat_capacity
		3935.2407570144424
		>>> containers[1].volume_Input({'volume': 0.00000153, 'temperature': 101.0, 'heat capacity': 5185.5, 'density': 1297.0}, 0.5)
		>>> containers[1].volume
		6.24238898038469e-06
		>>> containers[1].temperature
		275.13023440966043
		>>> containers[1].density
		1070.5295415653054
		>>> containers[1].heat_capacity
		4482.449038481635
		"""
		input_volume = float(input_liquid['volume'])
		input_temperature = float(input_liquid['temperature'])
		input_heat_capacity = float(input_liquid['heat capacity'])
		input_density = float(input_liquid['density'])
		input_mass = input_density*input_volume
		
		old_mass = self.mass()
		old_temp = self.temperature
		old_volume = self.volume
		
		total_energy = old_mass*old_temp*self.heat_capacity+input_density*input_volume*input_temperature*input_heat_capacity
		
		self.heat_capacity = (old_mass*self.heat_capacity+input_volume*input_density*input_heat_capacity)/(old_mass+input_density*input_volume)#Don't know if right but weighted average of heat capcity by mass
		self.density = (old_mass+input_volume*input_density)/(old_volume+input_volume)
		self.volume = old_volume+input_volume
		self.temperature = total_energy/(self.heat_capacity*self.mass())
		
	
	def volume_Output(self, delta_time):
		"""
		Calculates the volume output of the container and returns it in the apropiat format.
		
		>>> containers=Get_Test_Containers()
		>>> containers[0].volume_Output(0.5)
		{'volume': 0.0, 'temperature': 293.0, 'heat capacity': 4185.5, 'density': 997.0}
		>>> containers[3].volume_Output(0.5)
		{'volume': 0.00022619467105846513, 'temperature': 293.0, 'heat capacity': 4185.5, 'density': 997.0}
		>>> containers[4].volume_Output(0.5)
		{'volume': 1.5000000000000002e-09, 'temperature': 293.0, 'heat capacity': 4185.5, 'density': 997.0}
		"""
		output_liquid = {'volume':self.pump*delta_time+max([self.volume-self.volume_capacity, 0.0]), 'temperature': self.temperature, 'heat capacity': self.heat_capacity, 'density': self.density}
		
		self.volume = self.volume-output_liquid['volume']
		
		return output_liquid



def Get_Test_Containers():
	"""
	Gets containers for testing. Also does the testing for the init
	
	>>> containers=Get_Test_Containers()
	>>> containers[0].ID
	0
	>>> containers[2].ID
	2
	>>> containers[4].pump
	3.0000000000000004e-09
	>>> containers[3].area_container
	0.002513274122871835
	>>> containers[2].area_container
	0.0018849555921538759
	>>> containers[4].volume_capacity
	1.570796326794897
	>>> containers[3].volume_capacity
	2.5132741228718347e-05
	>>> containers[1].volume_capacity
	6.283185307179587e-06
	>>> containers[4].volume
	0.15707963267948968
	>>> containers[3].volume
	0.0002513274122871835
	>>> containers[1].volume
	4.71238898038469e-06
	>>> containers[1].temperature
	366.25
	>>> containers[0].temperature
	293.0
	>>> containers[1].temperature_container
	366.25
	>>> containers[0].temperature_container
	293.0
	"""
	lis = []
	
	lis.append(Container(0, 0.01, 0.01, 0.0025, 100, 293, 0))#Normal
	lis.append(Container(1, 0.01, 0.02, 0.0025, 75, 293*1.25, 0))#Nearly full and quite hot
	lis.append(Container(2, 0.03, 0.01, 0.0025, 10, 293, 0))#Nearly empty
	lis.append(Container(3, 0.02, 0.02, 0.0025, 1000, 293, 0))#Overfull
	lis.append(Container(0, 0.5*(2**0.5), 1, 0.0025, 10, 293, 3*(10**-9)))#Huge container with pump
	
	return lis
	
	

if __name__ == "__main__":
    import doctest
    doctest.testmod()