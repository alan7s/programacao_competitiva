import math
#PROBLEMA: 1036 - Fórmula de Bhaskara
values = input().split()
A=float(values[0])
B=float(values[1])
C=float(values[2])
delta=(B*B)-4*A*C
if(delta >= 0 and A!=0):
        R1 = ((B*-1)+math.sqrt(delta))/(2*A)
        R2 = ((B*-1)-math.sqrt(delta))/(2*A)
        print("R1 = {:.5f}".format(R1))
        print("R2 = {:.5f}".format(R2))
else:
        print("Impossivel calcular")
