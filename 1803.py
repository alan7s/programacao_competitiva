#PROBLEMA: 1803 - Matring
matriz = []
C = []
c = []
F = ''
L = ''
saida = ''
for i in range(80):
    C.append('')
    c.append(0)
for _ in range(4):
    linha = input()
    matriz.append([ord(char) - ord('0') for char in linha])
tamanho = len(linha)
N = tamanho - 2
for i in range(tamanho):
    for j in range(4):
        aux = chr(matriz[j][i] + ord('0'))
        if i == 0:
            F += aux
        elif i == tamanho - 1:
            L += aux
        else:
            C[i-1] += aux
f = int(F)
l = int(L)
for i in range(N):
    c[i] = int(C[i])
for i in range(N):
    saida += chr(((f * c[i]) + l) % 257)
print(saida)
