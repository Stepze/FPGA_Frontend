# -*- coding: utf-8 -*-
import json
import random
import time
from threading import Thread

class DummyApplicationLogic(Thread):
	def __init__(self,connection1,connection2,idx):
		Thread.__init__(self)
		self.setDaemon(True)
		self.connection1 = connection1
		self.connection2 = connection2
		self.id = idx
		self.connection1.register(self.id)
		self.connection2.register(self.id)

	def run(self):
		while True:
			self.receivedJSON = self.connection1.receive(self.id)
			if self.receivedJSON != "":
				print("application logic has received sth.")
				self.connection2.send(self.receivedJSON,self.id)


			self.receivedJSON = self.connection2.receive(self.id)
			if self.receivedJSON != "":
				self.connection1.send(self.receivedJSON,self.id)

				