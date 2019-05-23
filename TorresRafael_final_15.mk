TorresRafael_final_15.pdf : field.txt ex1.py
	python ex1.py
field.txt : a.out
	./a.out > field.txt
a.out : campo.cpp
	g++ campo.cpp