from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Gui_class(QMainWindow):
	def __init__(self,parent):
		QMainWindow.__init__(self)
		self.dataChanged = False
		self.mainWidget = QWidget()
		self.setCentralWidget(self.mainWidget)
		self.layout = QGridLayout()
		self.mainWidget.setLayout(self.layout)

		self.id1Box = QGroupBox("ID1")
		self.id1layout = QGridLayout()
		self.id1Box.setLayout(self.id1layout)

		self.text1 = QLabel("Feld A")
		self.text2 = QLabel("Feld C")
		self.text1Edit = QLineEdit("")
		self.text2Edit = QLineEdit("")
		self.submitButton = QPushButton("submit")

		self.id1layout.addWidget(self.text1,1,1)
		self.id1layout.addWidget(self.text2,2,1)
		self.id1layout.addWidget(self.text1Edit,1,2)
		self.id1layout.addWidget(self.text2Edit,2,2)
		self.layout.addWidget(self.id1Box,1,1)
		self.layout.addWidget(self.submitButton,2,1)
		self.submitButton.clicked.connect(self.submit)

		parent.announce_gui_element(self.text1Edit)
		parent.announce_gui_element(self.text2Edit)




	def submit(self):
		self.dataChanged = True
	def has_data_changed(self):
		if self.dataChanged == True:
			self.dataChanged = False
			return True
		else:
			return False
		
