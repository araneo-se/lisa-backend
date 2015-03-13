'''
Created on 13 mar 2015

@author: Johan Wettergren
'''

import sys
sys.path.append("../backend/")

import logging
from flask import Flask, request, abort
import geolookup
import smsprovider

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s', filename='/tmp/lisa-backend.log')

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/geoprovider/lookup', methods=['GET'])
def do_geolookup(ip):
	logging.info("GET /geolookup?ip=%s", ip)
	if ip is None:
		abort(400)
	return geolookup.lookup(ip)

@app.route("/smsprovider/send", methods=['POST'])
def send_message(recipient, message):
	logging.info("POST /smsprovider/send (%s, %s)", recipient, message)
	return smsprovider.send(recipient, message)

if __name__ == '__main__':
	app.run()