from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import json
from AbstractGuiController import AbstractGuiController
from threading import Thread


class QtGuiController(AbstractGuiController):
	def __init__(self,guifile,connection,idx):
		Thread.__init__(self)
		self.setDaemon(True)										
		self.id = idx
		self.connection = connection
		self.connection.register(self.id)
		layout_module = __import__(guifile)
		layout_class = getattr(layout_module,"Gui_class")
		self.qtwindow = layout_class()
		self.qtwindow.show()
		
		self.id_layout_dict = {1:self.qtwindow.text1, 2:self.qtwindow.text2,3:self.qtwindow.sendBackEdit}

	def read_data(self,idy):
		a = self.id_layout_dict.get(idy)
		if type(a) == QLabel:
			return a.text()
		elif type(a) == QLineEdit:
			return a.text()

	def write_data(self,idy,data):
		a = self.id_layout_dict.get(idy)
		if type(a) == QLabel:
			a.setText(str(data))

		elif type(a) == QLineEdit:
			a.setText(str(data))

	def run(self):
		c = self.read_data(3)
		while True:
			self.receivedJSON = self.connection.receive(self.id)
			if self.receivedJSON != "":
				self.write_data(2,str(self.receivedJSON))
			b = self.read_data(3)
			if b != "" and c != b:
				jsonDict = {"module":"test","component":"test","command":"test","value":b}
				jSONobj = json.JSONEncoder().encode(jsonDict)
				self.connection.send(jSONobj,self.id)
				c = b




