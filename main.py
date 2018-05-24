from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from QtGuiController import QtGuiController								#In this main file all the components are brought together to build an actual program.
from DirectConnection import DirectConnection							#In this program everything runs on the same machine, so only DirectConnection-objects 
from DummyApplicationLogic import DummyApplicationLogic					#are used.
from DummyDecodeLogic import DummyDecodeLogic

if __name__ == "__main__":												
	app = QApplication(sys.argv)
	connection1, connection2 = DirectConnection(), DirectConnection()
	decLog = DummyDecodeLogic(connection1,1)							
	appLog = DummyApplicationLogic(connection1,connection2,2)
	guictrl = QtGuiController("QtLayout",connection2,3)
	
	
	decLog.start()
	appLog.start()
	guictrl.start()
	sys.exit(app.exec_())



