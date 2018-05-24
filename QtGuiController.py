from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import json
from AbstractGuiController import AbstractGuiController
from threading import Thread


class QtGuiController(AbstractGuiController):								#Objects of this class are made to handle and display a QT-gui, as described in a gui-file.
	def __init__(self,guifile,connection,idx):
		Thread.__init__(self)
		self.setDaemon(True)												#Objects of this class are daemonic threads, that will terminate if the main thread terminates.									
		self.id = idx
		self.connection = connection
		self.connection.register(self.id)
		layout_module = __import__(guifile)									#The next lines import the file with the qt-layout during runtime.
		layout_class = getattr(layout_module,"Gui_class")
		self.qtwindow = layout_class()										#Here a new instance of the Window is made.
		self.qtwindow.show()
		
		self.id_layout_dict = {1:self.qtwindow.text1, 2:					#Here the layout dictionary is created which translates a certain gui element into a number
		self.qtwindow.text2,3:self.qtwindow.sendBackEdit} 					#through which it can be accessed.

	def read_data(self,idy):												#read_data() takes the id of a gui element and returns the data that is contained in that 
		a = self.id_layout_dict.get(idy)									#element. The type of the data depends on the type of the gui-element.
		if type(a) == QLabel:
			return a.text()
		elif type(a) == QLineEdit:
			return a.text()

	def write_data(self,idy,data):											#write_data() takes the id of a gui-element and the data that should be written to that element
		a = self.id_layout_dict.get(idy)									#and updates the corresponding gui-element to display that data.
		if type(a) == QLabel:
			a.setText(str(data))

		elif type(a) == QLineEdit:
			a.setText(str(data))

	def run(self):															#The run() method periodically checks all user-editable gui-elements for user input and 
		c = self.read_data(3)												#forwards that input in form of a JSON-object via its connection.
		while True:															#How that JSON-object is created still needs to be discussed. This is just for demonstrating
			self.receivedJSON = self.connection.receive(self.id)			#the principle.
			if self.receivedJSON != "":
				self.write_data(2,str(self.receivedJSON))
			b = self.read_data(3)
			if b != "" and c != b:
				jsonDict = {"module":"test","component":"test","command":"test","value":b}
				jSONobj = json.JSONEncoder().encode(jsonDict)
				self.connection.send(jSONobj,self.id)
				c = b




