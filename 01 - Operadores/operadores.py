"""
Programação Estruturada
15/08/2023

Operadores
"""

print("Olá, mundo!")
# nome = input("Informe seu nome: ")

print(print("Olá, mundo!"))

# idade = input("Informe sua idade: ")
# print(type(idade))

# Atribuição
x = 2
x = 3
x = x + 2
x += 2 #-> x = x + 2
x /= 4 #-> x = x / 4

# Aritméticos
x = 10
y = 2
z = -2
print(x+10)
print(x-10)
print(x*10)
print(x/10) # retorno sempre em float (número quebrado/decimal)!
print(x%10) # operador de módulo (resto da divisão)
print(x**10) # operador de potência
print(x//10) # divisão inteira

# Operações aritméticas com strings

print("Olá, " + "mundo!") # concatenação de strings
print(10 * "-") # um inteiro e uma string

# Comparação ou Relacionais
# Retornar com True ou False

print(x > y) #True
print(x < y) #False
print(x >= y)#True
print(x <= y)#False
print(x == y)#False
print(x != y)# True -> operador diferente
print(0 <= x <= 10) # True

print((x + 20) <=y * 2 != 10)

# Booleanos ou Lógicos

print(True and False)
print(True or False)
print(not True)

print(bool(10))

x = 10
y ="oi"

print(x and y)