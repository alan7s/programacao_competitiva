#PROBLEMA: 1253 - Cifra de César
n_casos = int(input())
for i in range(n_casos):
        setenca=list(input())
        n_pos=int(input()) #deslocamento -
        char=''
        for j in setenca:
                real_pos = ord(j) - n_pos #char to integer
                if(real_pos < 65):
                        aux=65-real_pos
                        char = char+chr(91-aux) #integer to char
                else:
                        char = char+chr(ord(j) - n_pos)
        print(char)
