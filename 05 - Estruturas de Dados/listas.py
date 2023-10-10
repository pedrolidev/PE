"""
Programação Estruturada
10/10/2023
"""

# Construção de listas
alunos = ["abc", "def", "ghi"]
lista = [1, 4,5, False, [1, 2, 3]] # Não é uma boa prática

# Acesso a elementos
print(alunos[1])
# print(alunos[3]) -> erro de índice
print(alunos[-1]) # último elemento da lista

# Matrizes
coordenadas = [
    [1, 2, 6],
    [1, 10],
    [-1, -5]
]
print(coordenadas[0][1])

# Slicing / Fatiamento
print("-" * 40)
alunos = ["abc", "def", "ghi", "jkl", "mno", "pqr"]
print(alunos[1:5])
print(alunos[1:6:2])
print(alunos[:4:2]) # Começa no início da lista
print(alunos[1::2]) # Termina no final da lista
print(alunos[1:])
print(alunos[::-1]) # Inverte a lista

# Operações com listas - Pertencimento
print("-" * 40)
print("def" in alunos)
print("stu" in alunos)
print("stu" not in alunos)

# Operações com listas - Soma
print([1, 2] + [3, 4])

# Operações com listas - Multiplicação
print([0] * 10)

# Operações com listas - Iteração
print("-" * 40)
for aluno in alunos:
    print(aluno)

for indice, aluno in enumerate(alunos):
    print(indice, aluno, sep=" - ")

notas = [7.5, 6.5, 8.2, 4.8, 6.4, 2.3]
for nota, aluno in zip(notas, alunos):
    print(aluno, nota, sep=": ")

# não é uma boa prático -> não é pythonico
for indice in range(len(alunos)):
    print(alunos[indice])

# Funções e Métodos com listas
print("-" * 40)
print(len(alunos))
alunos.append("stu") # sempre no final da lista
print(alunos)
alunos.insert(3, "vwx")
print(alunos)
alunos.extend(["yza", "bcd"])
print(alunos)

print("-" * 40)
alunos(alunos.pop())
print(alunos)
alunos(alunos.pop(3))
print(alunos)
alunos(alunos.remove("jkl")) # Remove a primeira ocorrência do elemento
print(alunos)

if "jkl" in alunos: # Caso contrário, pode subir um erro de valor
    alunos.remove("jkl")

print(alunos.index("mno"))

alunos = ["abc", "def", "abc", "Abc"]
print(alunos.count("abc"))

print(max(notas))
print(min(notas))
print(sum(notas))

print(notas)
notas_ord = sorted(notas)
print(notas)

notas.sort()
print(notas)

# Compreensão de listas
print("-" * 40)
numeros = [1, 2, 3, 4, 5, 6, 7]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2 for numeros in numeros)
    print(quadrados)

quadrado_impar = [numero ** 2 for numero in numeros if numero % 2 == 1]
print(quadrado_impar)

print(coordenadas)
# linearização de matrizes
coordenadas = [x for y in coordenadas for x in y]
print(coordenadas)

# Dados Mutáveis vs Imutáveis
print("-" * 40)
x = 2
y = x
x = 3
print(x, y)

a = [1]
b = a
a.append(2)
a[0] = 999
print(a, b)

def limpa_dados(lista, valor_a_limpar):
    for dado in lista:
        if dado == valor_a_limpar:
            lista.remove(dado)
    
    return lista

# print("-" * 40)
# nome = ["a", "b", "c", "a", "a", "d", "a" ]
# outros_nomes = limpa_dados(nomes, "a")
# print(outros_nomes)
# print(nomes)

print("-" * 40)
nomes = ["a", "b", "c", "a", "a", "d", "a" ]
novos_nomes = nomes.copy() # Gera uma nova lista, em outro endereço de memória
limpa_dados(novos_nomes, "a")
print(nomes)
print(novos_nomes)

print("-" * 40)
def adiciona_elemento(elem, lista=[]):
    if lista is None:
        lista = []
    lista.append(elem)
    return lista

a = [1, 2, 3]
adiciona_elemento(4, a)
adiciona_elemento(5, a)
adiciona_elemento(6, a)
print(a)

b = adiciona_elemento(8)
print(b)
b = adiciona_elemento(7)
print(b)

# Tuplas -> Listas Imutáveis
print("-" * 40)
tupla = (1, 2, 3, 4, 5)
print(tupla)
print(tupla[2])
print(tupla[0])
print(tupla[0:2])

def informa_nomes():
    nome1 = input("Informe um nome: ")
    nome2 = input("Informe outro nome: ")
    return nome1, nome2

nomes = informa_nomes()
print(nomes)
print(type(nomes))

primeiro_nome, segundo_nome = informa_nomes()
print(primeiro_nome, " - ", segundo_nome)