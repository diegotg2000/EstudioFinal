# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while', solamente puede usar 'slicing' (i.e. a[2:-2])
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])
a=fx[1:9]
b=fx[0:8]
c=fx[2:10]
h=2/10

segunda=(b + c - 2*a)/h**2

plt.plot(x[1:-1],segunda)
#plt.scatter(x,fx)
plt.savefig('Sderivada.png')


