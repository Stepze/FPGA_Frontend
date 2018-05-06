from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Gui_class(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.mainWidget = QWidget()
		self.setCentralWidget(self.mainWidget)
		self.layout = QGridLayout()
		self.mainWidget.setLayout(self.layout)

		self.text1 = QLabel("A")
		self.text2 = QLabel("B")
		self.layout.addWidget(self.text1,1,1)
		self.layout.addWidget(self.text2,2,1)


		self.sendBackEdit = QLineEdit("")
		self.layout.addWidget(self.sendBackEdit,3,1)

		
