# https://br.spoj.com/problems/TOMADA13/
linha = input()

# Separar os valores e atribuir para t1, t2, t3 e t4
valores = linha.split(" ") # Quebra a string em cada espaço em branco
# Converte para inteiro cada um dos valores e atribui para t1, t2, t3, t4
t1, t2, t3, t4 = [int(x) for x in valores]
print(t1 + t2 + t3 + t4 - 3)