I = int(input())

def epoca(I):
    ano = 0
    mes = 0
    dia = 0
    while I >= 365:
        I -= 365
        ano += 1
    while I >= 30:
        I -= 30
        mes += 1
    while I >= 1:
        I -= 1
        dia += 1
    print(ano, "ano(s)")
    print(mes, "mes(es)")
    print(dia, "dia(s)")

epoca(I)