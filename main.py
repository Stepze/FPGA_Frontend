from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from DummyGuiController import QTGuiController
from DummyConnection import DummyConnection
from DummyApplicationLogic import DummyApplicationLogic
from DummyDecodeLogic import DummyDecodeLogic

if __name__ == "__main__":
	app = QApplication(sys.argv)
	connection1, connection2 = DummyConnection(), DummyConnection()
	decLog = DummyDecodeLogic(connection1,1)
	appLog = DummyApplicationLogic(connection1,connection2,2)
	guictrl = QTGuiController("QtLayout",connection2,3)
	
	
	guictrl.qtwindow.show()
	
	decLog.start()
	appLog.start()
	guictrl.start()
	sys.exit(app.exec_())



