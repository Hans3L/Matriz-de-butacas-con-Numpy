import numpy as np
from helper import validacion
import matplotlib.pyplot as plt

c = 1
matriz2 = np.zeros((2, 10))
print(matriz2)

while c <= 20:
    print("Ingrese fila a escoger 1 o 2!")
    fila = int(input())
    print("Ingrese columna a escoger 1 al 10!")
    columna = int(input())

    if matriz2[fila - 1][columna - 1] == 0:
        matriz2[fila - 1][columna - 1] = 1
        # plt.plot(fila,columna)
        # plt.xlabel("fila")
        # plt.ylabel("columna")
        # plt.title("Butacas")
        #
        # plt.show()
        c = c+1
        print("Asiento Registrado")
        print(matriz2)
    else:
        print("Asiento Ocupado")
        print(matriz2)