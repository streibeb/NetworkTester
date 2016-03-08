#!/usr/bin/python
import os
import platform
import time
import datetime

FILE_PATH = 'NetworkOutages.csv'
SLEEP_TIME_MAX = 60
SLEEP_TIME_MIN = 5

def checkNetwork(hostname):
	startTime = datetime.datetime.now()
	endTime = startTime
	sleepTime = SLEEP_TIME_MAX
	networkWasDown = False
	while 1:
		if platform.system() == "Windows":
			response = os.system("ping "+hostname+" -n 1")
		else:
			response = os.system("ping -c 1 " + hostname)

		if response == 0: # Network is up
			print "Network is up!"
			if networkWasDown == True:
				networkWasDown = False
				endTime = datetime.datetime.now()
				sleepTime = SLEEP_TIME_MAX
				recordOutage(startTime, endTime)
		else: # Network is down
			print "Network is down!"
			if networkWasDown == False:
				networkWasDown = True
				startTime = datetime.datetime.now()
				sleepTime = SLEEP_TIME_MIN
		
		time.sleep(sleepTime)
	
def recordOutage(startTime, endTime):
	difference = endTime - startTime
	fd = open(FILE_PATH,'a')
	toWrite = str(startTime) + "," + str(endTime) + "," + str(difference)
	fd.write(toWrite)
	fd.close()

checkNetwork("www.google.com")