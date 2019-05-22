#Ejercicio4
# 'y' es una senal en funcion del tiempo 't' con las unidades descritas en el codigo.
# a. Grafique la senal en funcion del tiempo en la figura 'senal.png' ('y' vs. 't')
# b. Calule la transformada de Fourier (sin utilizar funciones de fast fourier transform) y
# grafique la norma de la transformada en funcion de la frecuencia (figura 'fourier.png')
# c. Lleve a cero los coeficientes de Fourier con frecuencias mayores que 10000 Hz y calcule 
# la transformada inversa para graficar la nueva senal (figura 'filtro.png')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

n = 512 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 128 ) #128 samples per frequency
t = np.linspace( 0, (n-1)*dt, n) 
T=(n-1)*dt
y = np.sin(2 * np.pi * f * t) + np.cos(2 * np.pi * f * t * t)
noise = 2*(np.random.rand(n)-0.5)
y  =  y + noise

plt.plot(t,y)
plt.savefig('senal.png')
plt.clf()

def transformada(y,n):
    i=complex(0,1)
    N=len(y)
    Z=np.exp(-2*np.pi*i/N)
    suma=0
    for k in range(N):
        suma+=y[k]*Z**(n*k)
    return suma

def inversa(y,n):
    i=complex(0,1)
    N=len(y)
    Z=np.exp(-2*np.pi*i/N)
    suma=0
    for k in range(N):
        suma+=y[k]*Z**(-n*k)
    return suma/N

nlist=np.arange(n)
trans=transformada(y,nlist)

plt.plot(2*np.pi*nlist/T , trans)
plt.savefig('fourier.png')
plt.clf()

trans[2*np.pi*nlist/T > 10000]=0
nueva=inversa(trans, nlist)

plt.plot(t, nueva)
plt.savefig('filtro.png')
plt.clf()
