#PROBLEMA: 2840 - Balão++
def volume_esfera(raio):
    volume = (4/3) * 3.1415 * raio ** 3
    return volume

entrada = input().split()
R = float(entrada[0])
L = float(entrada[1])
cont = 0
volume = volume_esfera(R)
litros = volume
while(litros <= L):
    cont = cont + 1
    litros = litros + volume
print(cont)
