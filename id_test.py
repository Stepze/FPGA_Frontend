# -*-coding: utf-8 -*-
from ID import ID



def test():
	a = ID.create_ids("Id_file")
	s = a[0].get_dependant_values("a",3.5)
	print(s)


if __name__ == "__main__":
	test()