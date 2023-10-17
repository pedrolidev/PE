def calculo_da_divisao():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        resultado = num1 / num2
    except ValueError:
        print("Erro: Certifique-se de inserir números inteiros válidos.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    else:
        print(f"O resultado da divisão de {num1} por {num2} é: {resultado:.2f}")
    finally:
        print("Operação concluída.")

calculo_da_divisao()
