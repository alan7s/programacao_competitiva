#PROBLEMA: 2591 - HameKameKa
n_casos = int(input())
for j in range(n_casos):
        poder=list(input())
        super=0
        aux=0
        char='k'
        for i in poder:
                if i == 'a':
                        super=super+1
                if i == 'k':
                        aux=super
                        super=0
        total=aux*super
        for i in range(total):
                char=char+'a'
        print(char)
