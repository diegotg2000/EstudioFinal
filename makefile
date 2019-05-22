grafica1.pdf: datos.dat graficas.py
	python graficas.py
datos.dat: datos.x
	./datos.x > datos.dat
datos.x: datos.cpp
	g++ datos.cpp -o datos.x