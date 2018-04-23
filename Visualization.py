
def Visualization():
	"""
	
	"""
	loop=True
	while loop:
		try:
			file=open(input('Filename: '), 'r')
			loop=False
		except FileNotFoundError:
			print('Unable to find file. Did you add the file extestion?')
		
		

Visualization()