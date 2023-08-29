"""
Programação Estruturada
29/08/2023

Funções
"""

# print("=" * 30)
# print("Relatório de despesas")
# print("=" * 30)

# print("=" * 30)
# print("Relatório de vendas")
# print("=" * 30)

# print("-" * 30)
# print("Dados de acesso")
# print("-" * 30)

# print("-" * 30)
# print("Quadro de pessoal")
# print("-" * 30)

def cabecalho(titulo, sep="-", tamanho=30):
    print(sep * 30)
    print(titulo)
    print(sep * tamanho)

# cabecalho("Relatório de despesas", "-", tamanho=25)
# cabecalho("Folha de ponto", tamanho=20, sep="*")

def soma(x, y):
    return x + y

# print(16 - soma(10, 12) * soma(1, 2))

# Escopo local vs escopo global de variáveis

a = 2 # escopo global
PI = 3.14 # caixa alta == constante

def func():
    global a # não é uma boa prática!
    a = 3 # escopo global
    print(a)

def func2():
    print(a)

# print(a)
# func()
# print(a)
# func2()

# Exercícios extra

# 1)
def media(ap1, ap2, ac):
    return (ap1 + ap2) * 0.4 + ac * 0.2

# 2)
def m_para_cm(comp_m):
    return comp_m * 100

# 3)
def conversao(fahrenheit):
    return (fahrenheit - 32) / 9 * 5

def main():
    print(media(8, 8, 10))
    print(m_para_cm(4.5))
    print(conversao(182))

main()