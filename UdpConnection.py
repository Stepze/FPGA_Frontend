# -*-coding: utf-8 -*-
from AbstractConnection import AbstractConnection
from threading import Thread
import socket
import json

class UdpConnection(AbstractConnection,Thread):
	def __init__(self,ip,port):
		Thread.__init__(self)
		self.setDaemon(True)
		self.jsonList = []
		self.id1 = -1
		self.ip = ip
		self.port = port
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRM)
		self.socket.bind(self.ip, self.port)

	def register(self,idx):
		if idx != self.id1 and self.id1 == -1:
			self.id1 = idx
	
	def send(self,jsonObj,idx):
		if idx == self.id1:
			socket.send(str(jsonObj))
		else:
			raise Exception("unknown id")

	def receive(self,idx):
		if idx == self.id1:
			return self.jsonList.pop(0)
		else:
			raise Exception("unknown id")

	def run(self):
		while True:
			data = self.socket.recv(1024)
			self.jsonList.append(json.loads(data))



