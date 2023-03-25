#PROBLEMA: 1235 - De Dentro para Fora
n = int(input())
for i in range(n):
        linha = list(input())
        saida = ''
        metade = int(len(linha)/2)
        primeira = linha[:metade]
        segunda = linha[metade:]
        primeira.reverse()
        segunda.reverse()
        print(''.join(primeira + segunda))
