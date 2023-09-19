# https://br.spoj.com/problems/DADINHOS/

def le_parametros_entrada():
    # Ler uma linha
    linha = input()

    # Separar os valores e atribuir para n, c e d
    valores = linha.split(" ") # Quebra a string em cada espaço em branco
    # Converte para inteiro cada um dos valores e atribui para n, c e d
    return [int(x) for x in valores]

def verifica_condicao_parada(n, c, d):
    return n == c == d == 0

def main():
    while True:
        n, c, d = le_parametros_entrada()

        # Verificar se n, c e d são iguais a zero
        if verifica_condicao_parada(n, c, d):
            break

        print(n * c * d)

main()