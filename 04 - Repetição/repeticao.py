"""
Programação Estruturada
12/09/2023
"""

def contagem_regressiva(num):
    while num > 0:
        print(num)
        num -= 1

# contagem_regressiva(5)

def pede_nome():
    nome = input("Informe o seu nome: ")

    while nome == "":
        nome = input("O texto passado é inválido! Informe um nome: ")

        print("Olá", nome)

# pede_nome()

def numero():
    while True:
        numero = int(input("Informe um número: "))

        if numero == 5:
            break # interrompe por completo a estrutura de repetição

# numero()


def tentativas():
    num_tentativas = 0

    while num_tentativas < 3:
        nome = input("Informe um nome: ")

        if nome != "":
            print("Olá", nome)
            break

        num_tentativas += 1
    else: # só vai ser executado casa não tenha passado pelo break
        print("Nenhum nome foi inserido")
        nome = "erro"

    print(nome)

tentativas()

# tentativas()

def contagem_regressiva2(num):
    for cont in range(num, 0, -1): # 5 4 3 2 1 (pq o -1 faz ser do maior ao menor, ordem crescente)
        print(cont)

contagem_regressiva2(5)

def imprime_texto():
    for _ in range(5): # 0 1 2 3 4
        print("texto")

# imprime_texto()

# 1)
def conta_pares(min, max):
    if min %2 != 0:
        min += 1

    if max % 2 != 0:
        max -= 1

    for num in range(min, max + 1, 2):
        if num < max:
            print(num, end=" - ")
        else:
            print(num)

# conta_pares(1, 7)
# print("-" * 20)
# conta_pares(2, 6)
# print("-" * 20)
# conta_pares(2, 7)
# print("-" * 20)
# conta_pares(1, 6)
# print("-" * 20)

#  2)
def conta():
    user = input("Digite seu usuário: ")

    while True:
        password = input("Digite sua senha: ")
        if user != password:
            break

        print("Erro! Seu nome e senha precisam ser diferentes!")

conta()