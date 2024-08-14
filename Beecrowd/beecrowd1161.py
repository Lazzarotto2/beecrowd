from math import factorial


def main():
    try:
        while True:
            # Ler a linha de entrada
            linha = input()
            # Verificar se a linha está vazia (EOF)
            if not linha:
                break

            # Dividir a linha em dois valores
            valores = linha.split()
            # Converter os valores para inteiros
            M = int(valores[0])
            N = int(valores[1])

            # Calcular a soma dos fatoriais de M e N
            soma_fatoriais = factorial(M) + factorial(N)

            # Imprimir o resultado
            print(soma_fatoriais)
    except EOFError:
        pass


if __name__ == "__main__":
    main()