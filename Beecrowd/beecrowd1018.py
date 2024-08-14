

def numero_notas(x):
    nota1 = 0
    nota2 = 0
    nota3 = 0
    nota4 = 0
    nota5 = 0
    nota6 = 0
    nota7 = 0
    valor_inicial = x

    while x >= 100:
        nota1 += 1
        x -= 100
    while x >= 50:
        nota2 += 1
        x -= 50
    while x >= 20:
        nota3 += 1
        x -= 20
    while x >= 10:
        nota4 += 1
        x -= 10
    while x >= 5:
        nota5 += 1
        x -= 5
    while x >= 2:
        nota6 += 1
        x -= 2
    while x >= 1:
        nota7 += 1
        x -= 1
    print(valor_inicial)
    print(nota1, "nota(s) de R$ 100,00")
    print(nota2, "nota(s) de R$ 50,00")
    print(nota3, "nota(s) de R$ 20,00")
    print(nota4, "nota(s) de R$ 10,00")
    print(nota5, "nota(s) de R$ 5,00")
    print(nota6, "nota(s) de R$ 2,00")
    print(nota7, "nota(s) de R$ 1,00")




x = int(input())
numero_notas(x)