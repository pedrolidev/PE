def parametro_print(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='   ')
        print()

n = int(input("Digite o valor de n: "))
parametro_print(n)
