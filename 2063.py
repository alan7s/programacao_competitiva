#PROBLEMA: 2063 - Caçando Digletts
def mdc(n1,n2):
        resto = n1 % n2
        while (resto != 0):
                n1 = n2
                n2 = resto
                resto = n1 % n2
        return n2

qnt_buracos = int(input())
buracos = [0]*105
linha = [int(x) for x in input().split()]
buracos[:len(linha)] = linha
tempo = 0
resp = 1
for i in range(qnt_buracos):
        tempo = 1
        buraco = buracos[i]
        while(buraco != i+1 ):
                tempo = tempo + 1
                buraco = buracos[buraco-1]
        resp = (resp / mdc(resp, tempo)) * tempo
print(int(resp))
