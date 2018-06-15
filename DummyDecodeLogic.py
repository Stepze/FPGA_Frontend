# -*- coding: utf-8 -*-
import json
import random
import time
from threading import Thread

class DummyDecodeLogic(Thread):											#Objects of this class mark the beginning of the information chain in this frontend.							
																		#This dummy-class is designed so that its objects create a JSON-object in a random time
	def __init__(self,connection,idx):									#from 0 to 10 seconds. These are then forwarded via its connection.
		Thread.__init__(self)
		self.setDaemon(True)										
		self.connection = connection
		self.id = idx
		self.connection.register(self.id)
		self.receivedJSON = ""
		

	def run(self):
		commandList = [5,132]
		while True:
			time.sleep(random.randrange(0,10))							#sleep for a random time in the range of 0...10 seconds
			module = random.randrange(0,2)								#then create a json object with random content
			component = random.randrange(0,24)
			command = random.choice(commandList)
			value = random.randrange(4000000000,5000000000)
			
			jsonDict = {"module":module,"component":component,
			"command":command,"value":value}
			self.decodedJSONobj = json.JSONEncoder().encode(jsonDict)
			self.connection.send(self.decodedJSONobj,self.id)			#send the json object

			self.receivedJSON = self.connection.receive(self.id)		#look for a json object to receive and print it as proof that it was received
			if self.receivedJSON != "":
				print(self.receivedJSON)
				self.receivedJSON = ""






