# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class AbstractConnection(ABC):		#abstract class to show the usage of the connection interface.
	
	@abstractmethod					#Both ends of the connection are needed to have an unique id,
	def register(self):				#with which they register at the connection object so that it
		pass						#knows both its partners and does not provide any information to a third one.

	@abstractmethod					#This is the method used to send a JSON-object to the other partner
	def send(self):					#The JSON object and the id of the sender have to be given.
		pass

	@abstractmethod					#This is the method used to receive a JSON-object from the other partner
	def receive(self):				#The id of the receiver has to be given.
		pass
