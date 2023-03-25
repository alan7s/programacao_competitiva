#PROBLEMA: 2286 - Par ou Ímpar
n = int(input())
teste = 1
while n != 0:
        jogador1 = input()
        jogador2 = input()
        print("Teste",teste)
        for i in range(n):
                mao = input().split()
                j1 = int(mao[0])
                j2 = int(mao[1])
                soma = j1 + j2
                if soma % 2 == 0:
                        print(jogador1)
                else:
                        print(jogador2)
        print("")
        n = int(input())
        teste = teste + 1
