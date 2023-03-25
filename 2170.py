#PROBLEMA: 2170 - Juros do Projeto
cont = 0
while True:
        try:
                cont=cont+1;
                leitura = input().split()
                print("Projeto {}:".format(cont))
                capital_inicial = float(leitura[0])
                retorno = float(leitura[1])
                juros = ((retorno - capital_inicial) / capital_inicial)*100
                print("Percentual dos juros da aplicacao: {:.2f} %".format(juros))
                print()
        except EOFError:
                break
