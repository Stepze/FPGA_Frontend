# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from threading import Thread

class AbstractGuiController(ABC,Thread):
	@abstractmethod
	def read_data(self):
		pass

	@abstractmethod
	def write_data(self):
		pass

	@abstractmethod
	def run(self):
		pass