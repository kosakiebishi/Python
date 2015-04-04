#!/usr/bin/env python

csvf = '/usr/local/sbin/list.csv'
#color = '1;32;40'
color = '1;37;40'
res = '1500x800'

import csv
import os
import sys

def getServList():
	serv = []
	with open(csvf, 'rb') as csvFile:
		doc = csv.DictReader(csvFile)
		for row in doc:
			serv.append(row)
	return serv


def connect2Server(system, ip, host, user):
	if ip == '' or system == '':
		print "Auf Wiedersehen"
		sys.exit()
	if system.lower() == 'w':
		print "\n\t Windows: \t %s, %s, %s \n\n" %(ip, host, user)
		# rdesktop - linux
		print 'rdesktop -u ' + user + " -g " + res + " " + ip
		os.system('rdesktop -u ' + user + " -g " + res + " " + ip)
		# mstsc - windows
		# os.system('mstsc /v:' + ip)
	elif system.lower() == 'l':
		print "\n\tLinux: \t %s, %s, %s \n\n" %(ip, host, user)
		os.system("ssh " + user + "@" + ip)
	else:
		system.exit()

def chooseServer(serv):
	for i in range(len(serv)):
		if i % 2 == 0:
			print "%-3i)  %s - %-40s -- %-20s - %s" %(i, serv[i]['Os'], serv[i]['Name'], serv[i]['Address'], serv[i]['AltAdd'])
		else:
			print '\x1b[%sm%-3i)  %s - %-40s -- %-20s - %s\x1b[0m' % (color, i, serv[i]['Os'], serv[i]['Name'], serv[i]['Address'], serv[i]['AltAdd'])	
	select = int(raw_input("\n - Server Number: "))
	connect2Server(serv[select]['Os'], serv[select]['Address'], serv[select]['Name'], serv[select]['User'])
	
	
chooseServer(getServList())


