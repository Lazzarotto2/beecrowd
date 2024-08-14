def somas():
    num1 = int(input())
    num2 = int(input())

    soma = 0
    if num2 > num1:
        for contagem in range(num1, num2 + 1):
            if contagem % 13 == 0:
                continue
            soma += contagem


    if num1 > num2:
        for contagem in range(num2, num1 + 1):
            if contagem % 13 == 0:
                continue
            soma += contagem
    print(soma)


somas()
