# -*-coding: utf-8 -*-
from AbstractConnection import AbstractConnection
from threading import Thread
import socket
import time
import json
import pickle

class UdpConnection(AbstractConnection,Thread):
	def __init__(self,ip,receiveport,destinationport):
		Thread.__init__(self)
		self.setDaemon(True)
		self.jsonList = []
		self.id1 = -1
		self.ip = ip
		self.recvPort = receiveport
		self.destPort = destinationport
		self.recvSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.recvSock.bind(("",self.recvPort))
		self.sendSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		
		
	def register(self,idx):
		if idx != self.id1 and self.id1 == -1:
			self.id1 = idx
	
	def send(self,jsonObj,idx):
		if idx == self.id1:
			
			self.sendSock.sendto(str(jsonObj).encode(), (self.ip,self.destPort))
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
			data = self.recvSock.recv(1024)
			self.jsonList.append(json.loads(data.decode('utf-8')))
			time.sleep(0.1)



