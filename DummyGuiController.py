from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from threading import Thread


class QTGuiController(Thread):
	def __init__(self,guifile,connection,idx):
		Thread.__init__(self)
		self.id = idx
		self.connection = connection
		self.connection.register(self.id)
		layout_module = __import__(guifile)
		layout_class = getattr(layout_module,"Gui_class")
		self.qtwindow = layout_class()
		
		self.id_layout_dict = {1:self.qtwindow.text1, 2:self.qtwindow.text2}

	def read_data(self,idy):
		a = self.id_layout_dict(idy)
		if type(a) == QLabel:
			return a.text()

	def write_data(self,idy,data):
		a = self.id_layout_dict.get(idy)
		if type(a) == QLabel:
			a.setText(str(data))

	def run(self):
		while True:
			self.receivedJSON = self.connection.receive(self.id)
			if self.receivedJSON != "":
				self.write_data(2,str(self.receivedJSON))