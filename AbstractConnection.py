# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class AbstractConnection(ABC):
	@abstractmethod
	def register(self):
		pass

	@abstractmethod
	def send(self):
		pass

	@abstractmethod
	def receive(self):
		pass
