#Problema:  3068 - Meteoros
teste = 0
while True:
    entrada = input().split()
    x1 = int(entrada[0])
    y1 = int(entrada[1])
    x2 = int(entrada[2])
    y2 = int(entrada[3])
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    teste = teste + 1
    n_meteoritos = int(input())
    meteoritos = []
    for i in range(n_meteoritos):
        pos_meteoritos = input().split()
        x = int(pos_meteoritos[0])
        y = int(pos_meteoritos[1])
        meteoritos.append((x, y))
    count = 0
    for x, y in meteoritos:
        if x1 <= x <= x2 and y2 <= y <= y1:
            count = count + 1
    print("Teste",teste)
    print(count)
