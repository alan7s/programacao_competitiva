#PROBLEMA: 2653 - Dijkstra
separa_joia = set()
quantidade_joias = 0
while True:
    try:
        joia = input().strip()
        separa_joia.add(joia)
    except EOFError:
        break
quantidade_joias = len(separa_joia)
print(quantidade_joias)
