from UdpConnection import UdpConnection
from DummyConnection import DummyConnection
from DummyApplicationLogic import DummyApplicationLogic
from DummyDecodeLogic import DummyDecodeLogic
import time
import sys

if __name__ == "__main__":
	connection1, connection2 = DummyConnection(), UdpConnection("127.0.0.1", 40000,40001)
	decLog = DummyDecodeLogic(connection1, 1)
	appLog = DummyApplicationLogic(connection1, connection2, 2)
	
	decLog.start()
	appLog.start()
	connection2.start()
	while True:
		time.sleep(1)