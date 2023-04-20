#PROBLEMA: 1039 - Flores de Fogo
from math import sqrt

while True:
    try:
        entrada = input().split()
        r1 = float(entrada[0])
        x1 = float(entrada[1])
        y1 = float(entrada[2])
        r2 = float(entrada[3])
        x2 = float(entrada[4])
        y2 = float(entrada[5])
        x=(x2-x1)
        y=(y2-y1)
        distancia = sqrt(x**2 + y**2)
        if (r1 >= distancia+r2):
            print("RICO")
        else:
            print("MORTO")
    except EOFError:
        break
