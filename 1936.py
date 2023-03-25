#PROBLEMA: 1936 - Fatorial
def calcfatorial(n):
        if n == 0:
                return 1
        else:
                return n*calcfatorial(n-1)

def maior(numero):
        cont=0
        resp=0
        while(resp<=numero):
                cont=cont+1
                resp=calcfatorial(cont)
        return cont-1

numero=int(input())
y=numero
fat=0
vetor=[]
while(fat!=numero):
        x=maior(y) #maior fatorial possivel 4! 1!
        vetor.append(x)
        fat=fat+calcfatorial(x) # 24 1
        y=numero-fat #quanto falta  1
print(len(vetor))
