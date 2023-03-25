#PROBLEMA: 2866 - Criptotexto
n_casos = int(input())
for i in range(n_casos):
        texto=list(input())
        char=''
        for i in texto:
                if(ord(i) > 96):
                        char=char+i
        print(char[::-1])
