# -*- coding: utf-8 -*-
import json
import random
import time
from threading import Thread

class DummyApplicationLogic(Thread):									#At the moment this is a dummy-class which objects just forward the received JSON-objects
	def __init__(self,connection1,connection2,idx):						#in both directions.
		Thread.__init__(self)
		self.setDaemon(True)
		self.connection1 = connection1
		self.connection2 = connection2
		self.receivedJSON = ""
		self.id = idx
		self.connection1.register(self.id)
		self.connection2.register(self.id)

	def run(self):														
		while True:
			self.receivedJSON = self.connection1.receive(self.id)		#receive a JSON-object from connection1 and forward it, if it is not empty
			if self.receivedJSON != "":
				print(self.receivedJSON)
				self.connection2.send(self.receivedJSON,self.id)


			self.receivedJSON = self.connection2.receive(self.id)		#do the same thing for connection2
			if self.receivedJSON != "":
				self.connection1.send(self.receivedJSON,self.id)

			time.sleep(0.5)
				