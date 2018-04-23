import math
import numpy as np
import pandas as pd
import os

from Simulation import Simulation
from Simulation import Get_Simple_Simulation
from Container import Container

class Controller:
	def __init__(self, simulation, CSV_export_settings):
		"""
		
		>>> con = Controller(Get_Simple_Simulation(), [True, 'Controller_test.csv', 2, 400])
		>>> os.remove('Controller_test.csv')
		"""
		self.sim = simulation
		
		self.CSVexport=CSV_export_settings[0]
		if self.CSVexport:
			self.file=open(CSV_export_settings[1], 'w')
			
			header='time'
			for con in self.sim.containers:
				extra=''
				for specific in [' volume', ' volume capacity', ' temperature', ' temperature container']:
					extra = extra+', '+str(con.ID)+specific
				header = header+extra
			
			self.file.write(header+'\n')
			
			for i in range(round(CSV_export_settings[3]/CSV_export_settings[2])+1):
				self.run_until_time(i*CSV_export_settings[2])
				self.CSV_export_data()
			
			self.file.close()
	
	def run_amount_of_ticks(self, amount):
		"""
		Runs the simulation a certain amount of ticks.
		
		>>> con = Get_Simple_Controller()
		>>> con.sim.time
		0.0
		>>> con.run_amount_of_ticks(200)
		>>> round(con.sim.time-con.sim.delta_time*200, 10)
		0.0
		"""
		for i in range(amount):
			self.sim.run_tick()
	
	def run_until_time(self, time):
		"""
		Runs the simulation a certain amount of ticks.
		
		>>> con = Get_Simple_Controller()
		>>> con.sim.time
		0.0
		>>> con.run_until_time(20)
		>>> round(con.sim.time, 10)
		20.0
		>>> con.sim.delta_time=0.0
		>>> con.run_until_time(40)
		Traceback (most recent call last):
		...
		ValueError: Delta time smaller than or equel to zero.
		>>> con.sim.delta_time=-10.0
		>>> con.run_until_time(40)
		Traceback (most recent call last):
		...
		ValueError: Delta time smaller than or equel to zero.
		"""
		if self.sim.delta_time<=0:
			raise ValueError('Delta time smaller than or equel to zero.')
		while float(time)>self.sim.time:
			self.sim.run_tick()
		
	def CSV_export_data(self):
		"""
		
		"""
		data_line=str(self.sim.time)
		
		for con in self.sim.containers:
			extra=', '+str(con.volume)+', '+str(con.volume_capacity)+', '+str(con.temperature)+', '+str(con.temperature_container)
			data_line=data_line+extra
		
		self.file.write(data_line+'\n')


def Get_Simple_Controller():
	return Controller(Get_Simple_Simulation(), [False, 'Controller_test.csv', 2, 400])

if __name__ == "__main__":
    import doctest
    doctest.testmod()