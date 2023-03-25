#PROBLEMA: 1516 - Imagem
while True:
        leitura = input().split()
        N = int(leitura[0])
        M = int(leitura[1])

        if (N == 0 and M == 0):
                break

        caracteres = []

        for i in range(N):
                itens = list(input())
                caracteres.append(itens[:M])

        #print(caracteres)

        leitura2 = input().split()
        A = int(leitura2[0])
        B = int(leitura2[1])

        loop = int(A/N)
        for j in range(N):
                linha = []
                qnt_impresso = int(B / len(caracteres[j]))
                for k in range(len(caracteres[j])):
                        for l in range(qnt_impresso):
                                linha.append(caracteres[j][k])
                for p in range(loop):
                        saida = ""
                        for x in linha:
                                saida = saida + x
                        print(saida)
        print()
