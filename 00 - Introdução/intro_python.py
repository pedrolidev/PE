"""
Docstring
Programação Estruturada
15/08/2023
Introdução a Python
"""
# Este é um comentário de código de uma linha.
print("Olá!") # Exibe na tela o texto "Olá".

"""
Esse é um comentário com várias linhas.
Posso inserir outra linha aqui.
"""

print("Olá, mundo!")
print("Olá!" ", mundo!")
print(15, "de agosto de", 2023)
print(15, "de agosto de", 2023, sep="-")

# Tipos de dados primitivos

# Numéricos - inteiros - int

print(4)
print(-10)

# Numéricos - decimais - float

print(3.65)
print(-12.156)

# Texto - string

print("Olá")
print('Olá')

# Booleanos - bool

print(True)
print(False)

# Utilizando caracteres de escape em strings

print("Olá, \"mundo!\"")
print("\\")
print('Olá, "mundo!"')
print("Olá,\nmundo!")

# Valor nulo - None

print(None)
print(print("olá!"))

# Lendo dados do usuário

# print(input("Digite o seu nome: "))
nome = input("Informe o seu nome: ")
print(nome)

nome = "Pedro"
print(nome)

# Estilo para indicação de constantes

PI = 3.14

print(type(nome))

# Typecasting

idade = int(input("Informe sua idade: "))
print(type(idade))