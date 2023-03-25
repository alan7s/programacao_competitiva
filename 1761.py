#PROBLEMA: 1761 - Decoração Natalina
import math
while True:
        try:
                values = input().split()
                A=float(values[0]) #angulo teodolito
                B=float(values[1]) #distancia da arvore
                C=float(values[2]) #altura elfo
                tan = math.tan(math.radians(A))
                altura=((B*tan)+C)*5
                print('{:.2f}'.format(altura))
        except EOFError:
                break
