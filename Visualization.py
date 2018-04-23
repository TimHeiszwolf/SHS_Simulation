import math
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import os
import imageio#https://packaging.python.org/tutorials/installing-packages/


def Visualization():
	"""
	
	"""
	loop=True
	while loop:
		try:
			print('WARNING: This program is going to make a lot of files in this folder so keep this in its own folder. It also requires about 25 MB of storage per 1000 datapoints.')
			filename=input('Filename: ')#'test.csv'
			file=open(filename, 'r')
			file.close()
			loop=False
		except FileNotFoundError:
			print('Unable to find file. Did you add the file extestion?')
	
	max_volume=float(input('Maximal y-value of volume: '))#4*10**-6
	min_temperature=float(input('Minimal y-value of temperature: '))#273
	max_temperature=float(input('Maximal y-value of temperature: '))#273+100
	
	time_of_gif=10#float(input('Length of gif: '))
	
	print('Now reading the data.')
	
	data=pd.read_csv(filename)
	amount_containers=int((data.shape[1]-1)/4)
	
	heat_images=[]
	volume_images=[]
	both_images=[]
	
	print('Now looping the data and making plots.')
	print('')
	
	for i in range(len(data)):
		containers=[]
		volumes=[]
		volumes_capacity=[]
		temperatures=[]
		
		for c in range(1,amount_containers):
			containers.append(c)
			volumes.append(data.loc[i][4*c+1])
			volumes_capacity.append(data.loc[i][4*c+2])
			temperatures.append(data.loc[i][4*c+3])
		
		df=pd.DataFrame({'Container': containers, 'Volume': volumes, 'Volume capacity': volumes_capacity, 'Temperature': temperatures})
		
		###THIS PART IS ABSOLUTE SHIT BUT IT GETS THE JOB DONE SO DON'T BITCH OR REWRITE IT YOURSELF!
		ax=df.plot(x='Container', y='Volume capacity', ylim=(0, max_volume), color='green')
		ax=df.plot(x='Container', y='Volume', ylim=(0, max_volume), color='blue', ax=ax)
		ax.set_xlabel='Container'
		ax.set_ylabel='volume'
		ax.text(0,0,'Time='+str(data.loc[i][0]))
		
		plt.savefig(str(data.loc[i][0])+'_volume.png')
		volume_images.append(str(data.loc[i][0])+'_volume.png')
		
		
		ax=df.plot(x='Container', y='Temperature', ylim=(min_temperature, max_temperature), color='red')
		ax.set_xlabel='Container'
		ax.set_ylabel='temperature'
		ax.text(0,0,'Time='+str(data.loc[i][0]))
		
		plt.savefig(str(data.loc[i][0])+'_temperature.png')
		heat_images.append(str(data.loc[i][0])+'_temperature.png')
		
		
		ax1=df.plot(x='Container', y='Temperature', ylim=(min_temperature, max_temperature), color='red')
		ax2=ax1.twinx()
		ax2=df.plot(y='Volume capacity', ylim=(0, max_volume), color='green', ax=ax2)
		ax2=df.plot(y='Volume', ylim=(0, max_volume), color='blue', ax=ax2)
		ax2.text(0,0,'Time='+str(data.loc[i][0]))
		
		plt.savefig(str(data.loc[i][0])+'_both.png')
		both_images.append(str(data.loc[i][0])+'_both.png')
		
		
		plt.close('all')
		
		print('Plotting '+str(round(100*i/len(data),3))+'% done.')
		
		#if i>100:
		#	break
	
	print('')
	print('Now making gifs.')#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
	
	names={'volume': volume_images, 'temperature': heat_images, 'both': both_images}
	
	for kind in ['volume', 'temperature', 'both']:
		images=[]
		for name in names[kind]:
			images.append(imageio.imread(name))
		output_file=kind+'.gif'
		imageio.mimsave(output_file, images, duration=time_of_gif/(len(data)*10))#Why doesn't the duration work properly?
	
	print('Now deleting the individual files.')
	
	for kind in ['volume', 'temperature', 'both']:
		for name in names[kind]:
			os.remove(name)
	
	print('Done!')
	
		
"""
def import_csv(file):
	content=file.readlines()
	content[0]=content[0].split(',').strip()
	
	pd.read_csv(file_countries)
	
	time=[]
	for i in range(1,len(contents)):
		content[i]=content[i].split(',').strip()
		time.append(float(content[i][0]))
	
	data={'time': time}
	amount_data_points=(len(content[0])-1)/4
	
	volume=[]
	volume_capacity=[]
	temperature=[]
	temperature_container=[]
	
	for i in range(amount_data_points):
		volume.append(float(content[4*i+1]))
		volume_capacity.append(float(content[4*i+2]))
		temperature.append(float(content[4*i+3]))
		temperature_container.append(float(content[4*i+4]))
	
	data['volume']=volume
	data['volume_capacity']=volume_capacity
	data['temperature']=temperature
	data['temperature_container']=temperature_container
	
	return data
"""

Visualization()