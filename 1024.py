#PROBLEMA: 1024 - Criptografia
n = int(input())
for k in range(n):
    frase = list(input())
    cont = 0
    while cont < 3:
        if cont == 0:
            for i in range(len(frase)):
                if (frase[i].isalpha()):
                    aux = ord(frase[i]) + 3
                    frase[i] = chr(aux)
        elif cont == 1:
             r_frase=reversed(frase)
             frase = list(r_frase)
#            print(frase)
        else:
            for i in range(int(len(frase) / 2), len(frase)):
                aux = ord(frase[i]) - 1
                frase[i] = chr(aux)
        cont = cont + 1
    saida = "".join(frase)
    print(saida)
