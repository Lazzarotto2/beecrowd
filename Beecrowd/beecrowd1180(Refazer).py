def menor_da_lista():
    quantidade = int(input())

    lista = [int(i) for i in input().split()]

    menor = [int(s) for s in lista]

    menor.sort()
    print("Menor valor: {}".format(menor[0]))
    for x, y in zip(list(range(0, quantidade)), lista):
        if y == menor[0]:
            print("Posicao: {}".format(x))


menor_da_lista()