"""
Programação Estruturada
2023.2
05/09/2023

Estruturas de seleção

if <teste>:
    <codigo>
else:
<codigo>

"""

def e_par(num):
    if num % 2 == 0:
        print(num, "é par")
    else:
        print(num, "é ímpar")

    print("fim da função")

# e_par(4)
# e_par(5)

def conceito(nota):
    if nota > 9:
        print("Conceito A")
    elif nota > 8:
        print("Conceito B")
    elif nota > 7:
        print("Conceito C")
    else:
        print("Conceito D")

# conceito(9.5)
# conceito(3.4)

def cli():
    opcao = input("Digite 1 para inserir nome, 2 para nota,"
                "ou qualquer outro caractere para sair: ")
    if opcao == "1":
        print("Opção 1")
    elif opcao == "2":
        print("Opção 2")
    else:
        print("Sair")
cli()

# Exercícios

# 1)
def e_par2(num):
    return num % 2 == 0

# 2)
def maior(num1, num2):
    if num2 > num2:
        return num1

    return num2

# Ternário
def maior2(num1, num2):
    return num1 if num1 > num2 else num2 if num1 < num2 else "são iguais"

# print(maior2(4, 9))
# print(maior2(11, 9))
# print(maior2(9, 9))

# 3)
def postivo(num):
    if num > 0:
        return"positivo"
    if num == 0:
        return "zero"

    return "negativo"

# 4)
def e_vogal(letra):
    if letra == "a" or letra ==  "e" or letra == "i" or letra == "o" or letra == "u":
        return "vogal"

    return "consoante"

# 5)
def media(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def resultados(m1, m2, m3):
    nota_media = media(m1, m2, m3)
    if nota_media == 10:
        return "Aprovado com distinção"
    elif nota_media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

m1 = float(input("Digite a primeira nota: "))
m2 = float(input("Digite a segunda nota: "))
m3 = float(input("Digite a terceira nota: "))

print(resultados(m1, m2, m3))



