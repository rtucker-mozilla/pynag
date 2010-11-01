#!/usr/bin/python
import os,sys

## This is for the custom nagios module
sys.path.insert(1, '../')
from pynag.Parsers import config

def is_ip(ip_address):
	import socket
	try:
		mm = socket.inet_aton(ip_address)
		return True # We got through that call without an error, so it is valid
	except socket.error:
		return False # There was an error, so it is invalid

## Create the plugin option
nc = config('/etc/nagios/nagios.cfg')
nc.parse()

nc.flag_all_commit()
nc.commit()

obj = nc.get_object('service','SNMP',user_key='name')

nc.print_conf(obj)



nc.commit()
