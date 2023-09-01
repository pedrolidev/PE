"""
José Pedro - AC2
01/09/2023

Exercício da AC
"""

# 1)
def calculo_salario(sal_hora, hora_mes):
    salario = sal_hora * hora_mes
    return salario

# 2)
def calc_operacao(n1, n2, n3):
    resultado1 = (2 * n1) * (n2 / 2)
    resultado2 = (3 * n1) + n3
    resultado3 = n3 ** 3

    print("O produto do dobro do primeiro com a metade do segundo é ", resultado1)
    print("A soma do triplo do primeiro com o terceiro é ", resultado2)
    print("O terceiro valor elevado ao cubo é", resultado3)

    n1 = float(input("Digite um valor para ser o primeiro número: "))
    n2 = float(input("Digite um valor para ser o segundo número: "))
    n3 = float(input("Digite um valor para ser o terceiro número: "))

# 3)
# Fiquei na dúvida de como se resolvia

def calcular_operacoes(num1, num2, num3):
    resultado1 = (2 * num1) * (num2 / 2)
    resultado2 = (3 * num1) + num3
    resultado3 = num3 ** 3

    return resultado1, resultado2, resultado3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado1, resultado2, resultado3 = calcular_operacoes(num1, num2, num3)

print(f"1) O produto do dobro do primeiro com metade do segundo é: {resultado1}")
print(f"2) A soma do triplo do primeiro com o terceiro é: {resultado2}")
print(f"3) O terceiro elevado ao cubo é: {resultado3}")

# 4)
def ser_bissexto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))



