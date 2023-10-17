def contador_de_digitos(numero):
    quantidade_digitos = len(str(numero))
    return quantidade_digitos

numero = int(input("Digite um número inteiro: "))
quantidade_de_digitos = contador_de_digitos(numero)
print("O número", numero, "tem", quantidade_de_digitos, "dígitos.")
