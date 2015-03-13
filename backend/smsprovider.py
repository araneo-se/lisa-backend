'''
Created on 13 mar 2015

@author: Johan Wettergren
'''

import re, random
import phonenumbers
from phonenumbers import PhoneNumberType, PhoneNumberFormat, NumberParseException

class smsprovider:
	'''
	classdocs
	'''

	@staticmethod
	def send(recipient, message):
		'''
		Pseudo-send a text message.
		- Phone number must be E.164 without leading zeros or plus sign, and must be a valid mobile phone number.
		- Text message must be shorter than 160 characters and will be ISO-8859-1 transliterated.
		- Operation will fail in 15% of the cases
		
		@return Boolean: True on pseudo-success
		'''

		if not re.match('/^[1-9][0-9]+$/', recipient):
			raise

		unicode = message.decode("utf-8")
		iso_message = unicode.encode("iso-8859-1", "ignore")

		if len(iso_message) > 160:
			raise

		try:

			# Parse the input phone number
			x = phonenumbers.parse(recipient, None)

			# Test for Fixed Line or Mobile
			if phonenumbers.number_type(x) != PhoneNumberType.MOBILE and phonenumbers.number_type(x) != PhoneNumberType.FIXED_LINE_OR_MOBILE:
				raise

		# ErrorType Exception
		except NumberParseException as e:
			raise

		if random.random() >= 0.15:
			return True
		else:
			return False
