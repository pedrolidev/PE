"""
José Pedro - AC4
12/09/2023

Exercícios da AC
"""

# 1)
def e_primo(num):
    if num < 2:
        return False

    primo = True
    for div in range(2, num):
        if num % div == 0:
            primo = False

    print("É primo?", primo)

e_primo(7)
e_primo(14)

# 2)
def calcula_parcelamento(divida):
    print("Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida")

    parcela1 = 1
    parcela2 = 3
    parcela3 = 6
    parcela4 = 9
    parcela5 = 12

    juros1 = 0
    juros2 = 10
    juros3 = 15
    juros4 = 20
    juros5 = 25

# Não soube desenvolver mais a partir desse ponto.


# 3)
def num_positivo():
    contagem_inicial = 0  # (0-25)
    contagem_semi_inicial = 0  # (26-50)
    contagem_intermediaria = 0  # (51-75)
    contagem_final = 0  # (76-100)

    while True:
        num = int(input("Digite um valor: "))

        if num < 0:
            break

        if 0 <= num <= 25:
            contagem_inicial += 1
        elif 26 <= num <= 50:
            contagem_semi_inicial += 1
        elif 51 <= num <= 75:
            contagem_intermediaria += 1
        elif 76 <= num <= 100:
            contagem_final += 1

    print("Números no intervalo (0-25): ", contagem_inicial)
    print("Números no intervalo (26-50): ", contagem_semi_inicial)
    print("Números no intervalo (51-75): ", contagem_intermediaria)
    print("Números no intervalo (76-100): ", contagem_final)

num_positivo()


