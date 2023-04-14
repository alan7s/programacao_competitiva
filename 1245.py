#PROBLEMA: 1245 - Botas Perdidas
def conta_pares(par_botas):
    cont = 0
    for chave, valores in par_botas.items():
        #print(valores)
        #print(cont)
        num_esquerdo = valores.count('E')
        num_direito = valores.count('D')
        if num_esquerdo == num_direito: #todos pares
            cont = cont + num_esquerdo
        elif num_esquerdo < num_direito: #ao menos 1 par
            cont = cont + num_esquerdo
        else: #ao menos 1 par esq > dir
            cont = cont + num_direito
    return cont
def mapeia_botas(botas):
    par = {}
    for i in range(0, len(botas), 2):
        chave = botas[i]
        valor = botas[i+1]
        if chave not in par:
            par[chave] = []
        par[chave].append(valor)
    return par
while True:
    try:
        N = int(input())
        calcados = []
        for i in range(N):
            entrada = input().split()
            calcados.append(int(entrada[0]))
            calcados.append(entrada[1])
        #print(calcados)
        pares=mapeia_botas(calcados)
        #print(pares)
        print(conta_pares(pares))
    except EOFError:
        break
