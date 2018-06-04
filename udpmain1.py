from UdpConnection import UdpConnection
from DirectConnection import DirectConnection
from DummyApplicationLogic import DummyApplicationLogic
from DummyDecodeLogic import DummyDecodeLogic
import time
import sys

if __name__ == "__main__":																		#This is one part of the netowrk-using program.
	connection1, connection2 = DirectConnection(), UdpConnection("127.0.0.1", 40000,40001)		#It is the part that contains the decode logic and the application logic
	decLog = DummyDecodeLogic(connection1, 1)													#The other other part is in a sepparate program.
	appLog = DummyApplicationLogic(connection1, connection2, 2)
	
	decLog.start()
	appLog.start()
	while True:
		time.sleep(1)