total = 0

for _ in range(2):
    x = input().split(" ")
    cod = int(x[0])
    qt = int(x[1])
    valor = float(x[2])
    total = total + qt*valor

print("VALOR A PAGAR: R$ %.2f" %total)