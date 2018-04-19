# -*- coding: utf-8 -*-
import json
import random
import time
from threading import Thread

class DummyDecodeLogic(Thread):

	def __init__(self,identifier,connection):
		Thread.__init__(self)
		self.connection = connection
		self.id = identifier
		self.connection.register(self.id)
		

	def run(self):
		commandList = [5,132]
		while True:
			time.sleep(random.randrange(0,10))		#sleep for a random time in the range of 0...10 seconds
			module = random.randrange(0,2)
			component = random.randrange(0,24)
			command = random.choice(commandList)
			value = random.randrange(4000000000,5000000000)
			
			jsonDict = {"module":module,"component":component,"command":command,"value":value}
			self.decodedJSONobj = json.JSONEncoder().encode(jsonDict)
			self.connection.send(self.decodedJSONobj,self.id)

			self.receivedJSON = self.connection.receive(self.id)
			if self.receivedJSON != "":
				self.receivedJSON = self.connection.jsonList[self.id]
				print(self.receivedJSON)
				self.receivedJSON = ""






