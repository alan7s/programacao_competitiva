#PROBLEMA: 3065 - Calculando
import re
n = int(input())
teste = 1
while n != 0:
        equacao=re.findall(r'\d+|\+|\-', input())
        #print(equacao)
        operacao = '+'
        aux = 0
        for i in equacao:
                if i == '+':
                        operacao = '+'
                elif i == '-':
                        operacao = '-'
                else:
                        if operacao == '+':
                                aux = aux + int(i)
                        elif operacao == '-':
                                aux = aux - int(i)
        print("Teste",teste)
        print(aux)
        print("")
        n = int(input())
        teste = teste + 1
