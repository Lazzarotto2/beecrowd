valor_pares = 0


for _ in range(5):
    valor = int(input())
    if valor % 2 == 0:
        valor_pares += 1


print(valor_pares, "valores pares")