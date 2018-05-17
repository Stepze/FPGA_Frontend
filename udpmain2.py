from UdpConnection import UdpConnection
from QtGuiController import QtGuiController
from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":
	app = QApplication(sys.argv)
	connection2 = UdpConnection("127.0.0.1", 40001,40000)
	guictrl = QtGuiController("QtLayout", connection2, 3)
	guictrl.qtwindow.show()
	connection2.start()
	guictrl.start()

	sys.exit(app.exec_())