#PROBLEMA: 2292 - Painel LED
N = int(input())
for k in range(N):
        leitura = input().split()
        led = list(leitura[0])
        C = int(leitura[1])
        j = 0
        while j < len(led):
                if led[j] == "X":
                        if(C % 2 != 0):
                                led[j] = 'O'
                        C = int(C / 2)
                else:
                        if(C % 2 == 0):
                                C = (C / 2)
                        else:
                                led[j] = 'X'
                                C = int(C / 2) + 1
                j = j + 1
        saida = "".join(led)
        print(saida)
