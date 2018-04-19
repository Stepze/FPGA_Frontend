# -*- coding: utf-8 -*-
import json
import random
import time
from threading import Thread

class DummyApplicationLogic(Thread):
	def __init__(self,identifier,connection):
		Thread.__init__(self)
		self.connection = connection
		self.id = identifier
		self.connection.register(self.id)

	def run(self):
		while True:
			self.receivedJSON = self.connection.receive(self.id)
			if self.receivedJSON != "":
				print("application logic has received:")
				print(self.receivedJSON)