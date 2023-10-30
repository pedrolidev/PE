import json

def dados_alunos():
    matricula = input("Insira sua matrícula: ")
    nome =  input("Insira o seu nome: ")
    email = input("Insira o seu e-mail: ")
    return matricula, {"nome": nome, "e-mail": email}

dados_alunos = {}

while True:
    matricula, dados = dados_alunos()
    dados_alunos[matricula] = dados
    prossiga = input("Quer adicionar mais um aluno? ")
    if prossiga != 's':
        break
    else:
        print("Aluno não encontrado!")

    print("Dados dos alunos foram salvos no arquivo .json.")