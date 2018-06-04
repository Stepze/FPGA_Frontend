from UdpConnection import UdpConnection
from QtGuiController import QtGuiController
from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":										#This is the other part of the network-using program.
	app = QApplication(sys.argv)								#It contains the gui controller and the layout.
	connection2 = UdpConnection("127.0.0.1", 40001,40000)
	guictrl = QtGuiController("QtLayout", connection2, 3)
	guictrl.start()

	sys.exit(app.exec_())