# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares mayores que 100 y que pare de imprimir al encontrar un numero primo.
import numpy as np

def esprimo(x):
    siono = True
    for n in range(2,int(np.sqrt(x))):
        if(x%n==0):
            siono=False
            break
    return siono

x = np.int_(np.random.random(100)*10000)

for i in x:
    if(i>100 and i%2==1):
        print(i)
    if(esprimo(i)):
        break



