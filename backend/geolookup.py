'''
Created on 13 mar 2015

@author: Johan Wettergren
'''

import csv
import socket, struct
import logging

class geolookup:
	'''
	classdocs
	'''

	store = "/tmp/lisabackend-geo.data"

	def __init__(self, params):
		'''
		Constructor
		'''

	def lookup(self, ip):

		num_ip = self.ip2long(ip)

		try:

			with open("../data/dbip-country.csv", 'r') as csvfile:
				reader = csv.reader(csvfile, delimiter=',', quotechar='"')
				for row in reader:
					range_start = self.ip2long(row[0])
					range_end = self.ip2long(row[1])
					if num_ip >= range_start and num_ip <= range_end:
						return row[2]

		except:
			raise

		# Not found
		raise

	@staticmethod
	def ip2long(ip):
		"""
		Convert an IP to a long.
		"""
		packedIP = socket.inet_aton(ip)
		return struct.unpack("!L", packedIP)[0]

