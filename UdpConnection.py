# -*-coding: utf-8 -*-
from AbstractConnection import AbstractConnection
from threading import Thread
import socket
import time
import json
import pickle
																				#Objects of this class are used to establish a connection between two parts of the program
class UdpConnection(AbstractConnection,Thread):									#running on different computers, connected via Ethernet. To get a working connection between					
																				#the splitup parts, each part needs to have a connection-object.So in this case there are
																				#2 connection objects needed for one physical connection in contrast to the direct 
																				#connection, where one object per connection was enough.

	def __init__(self,ip,rcvport,destport):										#Each connection object now only has one direct partner with an id. Instead of the second id					
		Thread.__init__(self)													#the connection object now needs to know on what port incoming packages will occur and to
		self.setDaemon(True)													#which ip-adress and what port outgoing packages should be forwarded.
		self.jsonList = []
		self.id1 = -1
		self.ip = ip
		self.recvPort = rcvport
		self.destPort = destport
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)			#A udp-socket object is used to handle the network traffic.
		self.sock.bind(("",self.recvPort))										#The port for incoming packages is bound to the socket.
		
		
		
	def register(self,idx):														#The register() method works just like the one in DirectConnection.py
		if idx != self.id1 and self.id1 == -1:									#but with the difference, that here only one partner needs to register,
			self.id1 = idx														#because the other one is on ther other side of the network.
	
	def send(self,jsonObj,idx):													#The send() method checks if the id of the sender is the registered one.
		if idx == self.id1:														#If that is the case, the JSON.object is encoded to to a byte-string																
			self.sock.sendto(str(jsonObj).encode(), (self.ip,self.destPort))	#and is then sent to the other end of the udp connection.
		else:
			raise Exception("unknown id")

	def receive(self,idx):														#The receive() method works just like the one in DirectConnection.py
		if idx == self.id1 and len(self.jsonList)>0:							#but with the difference that the buffer is only one-directional, because there is only
			return self.jsonList.pop(0)											#one partner directly connected. 
		elif idx == self.id1:
			return ""
		elif idx != self.id1:
			raise Exception("unknown id")

	def run(self):																#Since the connection needs to permanently look for incoming traffic at its port it needs
		while True:																#to be a thread, which receives the incoming data, decodes it ad appends it to the buffer.
			data = self.sock.recv(1024)
			self.jsonList.append(json.loads(data.decode('utf-8')))
			time.sleep(0.1)



