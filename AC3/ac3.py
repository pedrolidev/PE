"""
José Pedro - AC3
05/09/2023

Exercício da AC
"""

# 1)
def reajuste_salarial(salario):
    if salario <= 280:
        aumento_percentual = 20
    elif salario <= 700:
        aumento_percentual = 15
    elif salario <= 1500:
        aumento_percentual = 10
    else:
        aumento_percentual = 5

    aumento = (aumento_percentual / 100) * salario
    novo_salario = salario + aumento

    print("O salário desse funcionário antes do reajuste foi de: R$ ", salario)
    print("O percentual de aumento salarial aplicado sobre o recebimento desse funcionário foi de:  % ", aumento_percentual)
    print("O valor do aumento foi de: R$ ", aumento)
    print("O novo salário desse funcionário após o aumento foi de: R$ ", novo_salario)

salario = float(input("Digite o salário desse funcionário: "))
reajuste_salarial(salario)

# 2)
def semana(representacao):
    if representacao == 1:
        return "Domingo"
    elif representacao == 2:
        return "Segunda-feira"
    elif representacao == 3:
        return "Terça-feira"
    elif representacao == 4:
        return "Quarta-feira"
    elif representacao == 5:
        return "Quinta-feira"
    elif representacao == 6:
        return "Sexta-feira"
    elif representacao == 7:
        return "Sábado"
    else:
        return "Valor inválido"

representacao = int(input("Digite um número de 1 a 7: "))
print(semana(representacao))

# 3)
def raizes(a, b, c):
    if a == 0:
        print("A equação não é do segundo grau.")
        return

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Essa equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print("A equação possui uma raiz real: ", raiz)
    else:
        raiz1 = (-b + (delta)**0.5) / (2*a)
        raiz2 = (-b - (delta)**0.5) / (2*a)
        print("A equação possui duas raízes reais: ", raiz1, raiz2)

a = float(input("Insira o valor para a: "))
b = float(input("Insira o valor para b: "))
c = float(input("Insira o valor para c: "))
raizes(a, b, c)

