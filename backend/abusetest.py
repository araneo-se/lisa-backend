'''
Created on 13 mar 2015

@author: Johan Wettergren
'''

import shelve

class abusetest:
	'''
	classdocs
	'''


	def __init__(self, params):
		'''
		Constructor
		'''
		
	def lookup(self, ip):
		
		try:
			
			d = shelve.open(self.store)
			

			d.close()
		except:
			pass
		
					