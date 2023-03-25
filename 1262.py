#PROBLEMA: 1262 - Leitura Múltipla
while True:
        try:
                proc = list(input())
                P = int(input())
                pos = 0
                ciclos = 0
                n_processos = 0
                aux = 0
                while(pos < len(proc)):
                        ciclos = ciclos + 1
                        n_processos = 0
                        if(proc[pos] == 'W'):
                                pos = pos + 1
                        else:
                                aux = pos
                                while(aux < len(proc) and proc[aux] == 'R'):
                                        aux = aux + 1
                                        n_processos = n_processos + 1
                                        if(n_processos >= P):
                                                break
                                pos = aux
                                if(pos >= len(proc)):
                                        break
                print(ciclos)
        except EOFError:
                break
