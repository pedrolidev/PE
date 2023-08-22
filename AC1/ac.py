"""
José Pedro - AC1
22/08/2023

Exercícios da AC
"""
#1
# Atribuição de valores
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

# Cálculos
delta = b**2 - 4*a*c

raiz1 = (-b + delta ** 0.5) / (2*a)
print(bool(raiz1))
raiz2 = (-b - delta ** 0.5) / (2*a)

# Mensagem final para realizar o código
print("A primeira raiz equivale a", raiz1, "e a segunda raiz equivale a", raiz2)


#2
# Atribuição de valores
ano = int(input("Digite um ano: "))
multiplo_de_4 = (ano % 4) == 0
nao_multiplo_de_100 = (ano % 100) != 0
multiplo_de_400 = (ano % 400) == 0

bissexto = multiplo_de_4 and (nao_multiplo_de_100 or multiplo_de_400)

#Mensagem final para realizar o código
print(f"O ano {ano} é bissexto? {bissexto}")

