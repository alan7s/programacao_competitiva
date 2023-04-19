#PROBLEMA: 2518 - Escada do DINF
while True:
	try:
		N = float(input())
		entrada = input().split()
		H = float(entrada[0])
		C = float(entrada[1])
		L = float(entrada[2])
		hip = (H ** 2 + C ** 2) ** (1/2)
		area = hip * L
		result = (area * N)/10000
		saida = "{:.4f}".format(result)
		print(saida)
	except EOFError:
		break
