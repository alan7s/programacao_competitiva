#PROBLEMA: 1247 - Guarda Costeira
from math import sqrt, pow
while True:
        try:
                entrada = input().split()
                D = int(entrada[0])
                VF = int(entrada[1])
                VG = int(entrada[2])

                tempo = 1
                distancia = sqrt(pow(12, 2) + pow(D, 2))
                while True:
                                dist_VF = (VF*tempo)
                                dist_VG = (VG*tempo)
                                temp_VF = 12/dist_VF
                                temp_VG = distancia / dist_VG
                                if(dist_VF >= 12 and temp_VF < temp_VG):
                                        print("N")
                                        break
                                elif(dist_VG >= distancia and temp_VG <= temp_VF):
                                        print("S")
                                        break
                                elif(VF == 0 and VG == 0):
                                        print("S")
                                        break
                                tempo = tempo + 1
        except EOFError:
                break
