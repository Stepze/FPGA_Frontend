# -*- coding: utf-8 -*-

from DummyConnection import DummyConnection
from DummyDecodeLogic import DummyDecodeLogic
from DummyApplicationLogic import DummyApplicationLogic


def test():
	connection = DummyConnection()
	decoder = DummyDecodeLogic(1,connection)
	application = DummyApplicationLogic(2,connection)
	decoder.start()
	application.start()


if __name__ == "__main__":
	test()