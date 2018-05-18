# -*-coding: utf-8 -*-
from AbstractConnection import AbstractConnection
from threading import Thread
import socket
import time
import json
import pickle

class UdpConnection(AbstractConnection,Thread):
	def __init__(self,ip,rcvport,destport):
		Thread.__init__(self)
		self.setDaemon(True)
		self.jsonList = []
		self.id1 = -1
		self.ip = ip
		self.recvPort = rcvport
		self.destPort = destport
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind(("",self.recvPort))
		
		
		
	def register(self,idx):
		if idx != self.id1 and self.id1 == -1:
			self.id1 = idx
	
	def send(self,jsonObj,idx):
		if idx == self.id1:
			
			self.sock.sendto(str(jsonObj).encode(), (self.ip,self.destPort))
		else:
			raise Exception("unknown id")

	def receive(self,idx):
		if idx == self.id1 and len(self.jsonList)>0:
			return self.jsonList.pop(0)
		elif idx == self.id1:
			return ""
		elif idx != self.id1:
			raise Exception("unknown id")

	def run(self):
		while True:
			data = self.sock.recv(1024)
			self.jsonList.append(json.loads(data.decode('utf-8')))
			time.sleep(0.1)



