#PROBLEMA: 2287 - Proteja sua Senha
def encontrar_valor_comum(mapa, botoes):
        saida = []
        for i in range(len(botoes[0])):
                valores = []
                for j in range(len(botoes)):
                        chave = botoes[j][i]
                        valores.append(mapa[j][chave])
                for valor in valores[0]:
                        if all(valor in sublista for sublista in valores):
                            saida.append(valor)
                            break
        return saida

def mapeia_senha(vdigitos):
        tam = len(vdigitos) // 5
        mapeamento = {}
        for i in range(len(vdigitos)):
                letra = chr(ord('A') + i // tam)
                if letra not in mapeamento:
                        mapeamento[letra] = []
                mapeamento[letra].append(vdigitos[i])

        # exibição do mapeamento
#       for letra, valores in mapeamento.items():
#               print(f'{letra}: {valores}')
        return mapeamento

N = int(input())
teste = 1

while N != 0:
        digitos = [[] for _ in range(N)]
        botoes = [[] for _ in range(N)]
        mapa = [[] for _ in range(N)]
        for i in range(N):
                aux = input().split()
                for j in range(len(aux)):
                        if aux[j].isdigit():
                                digitos[i].append(int(aux[j]))
                        else:
                                botoes[i].append(aux[j])

                mapa[i] = mapeia_senha(digitos[i])

        #print(botoes)
        #print(mapa)

        resultado = encontrar_valor_comum(mapa, botoes)
        print("Teste",teste)
        print(' '.join(map(str, resultado)),end=' ')
        print("")
        print("")
        N = int(input())
        teste = teste + 1
