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
		self.qtwindow = layout_class(self)									#Here a new instance of the Window is made.
		self.qtwindow.show()
		
		self.id_layout_dict = {}											#Here the layout dictionary is created which translates a certain gui element into a number
																			#through which it can be accessed.
		 					

	def announce_gui_element(self,element):										#The GuiController is the parent of the Layout class
		try:
			i = len(self.id_layout_dict)+1										#Each gui-element has to announce itself, to fill the dictionary
			self.id_layout_dict.update({i:element})
		except:
			i=1
			self.id_layout_dict = {i:element}
		



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

	def run(self):															#The run() method periodically checks all user-editable gui-elements for user input and 										#forwards that input in form of a JSON-object via its connection.
		while True:															#How that JSON-object is created still needs to be discussed. This is just for demonstrating
			self.receivedJSON = self.connection.receive(self.id)			#the principle.
			print(self.receivedJSON)
			if self.receivedJSON != "":
				self.write_data(2,str(self.receivedJSON))
			if self.qtwindow.has_data_changed() == True:
				for key,value in self.id_layout_dict:
					b = self.read_data(key)
					if b != "":
						jsonDict = {"module":"ID1","component":"test","command":"test","value":b}
						jSONobj = json.JSONEncoder().encode(jsonDict)
						self.connection.send(jSONobj,self.id)
		



