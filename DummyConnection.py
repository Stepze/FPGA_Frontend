# -*- coding: utf-8 -*-
import json


class DummyConnection():
	def __init__(self):										
		self.jsonList = [[],[]]												
		self.id1 = -1
		self.id2 = -1
	
	def register(self,idx):
		if idx not in [self.id1,self.id2] and (self.id1 == -1 or self.id2 == -1):
			if self.id1 == -1:
				self.id1 = idx
			else:
				self.id2 = idx	
	

	def send(self,jsonobj,idx):																#self.jsonList[0] holds the values from partner one send to partner two and self.jsonList[1] vice versa
		if idx == self.id1:
			self.jsonList[0].append(jsonobj)
		elif idx == self.id2:
			self.jsonList[1].append(jsonobj)
		else:
			raise Exception("unknown id")

	def receive(self,idx):																	#here it is the other way round
		if idx == self.id1 and len(self.jsonList[1]) > 0:
			return self.jsonList[1].pop()
		elif idx == self.id2 and len(self.jsonList[0]) > 0:
			return self.jsonList[0].pop()
		elif idx != self.id1 and idx != self.id2:
			raise Exception("unknown id")
		else:
			return ""

		

