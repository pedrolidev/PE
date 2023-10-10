"""
Programação Estruturada
10/10/2023

Estruturas de Dados
Conjuntos:
    - Mutáveis
    - Não ordenados
    - Únicos
    - Não suporta indexação
    - Dicionários
"""

numeros = [1, 8, 5, 1, 2, 6, 1, 2, 8, 4, 3]
numeros_unicos = set(numeros)
numeros_unicos.add(9)
numeros_unicos.add(8)
numeros_unicos.add(0)
print(numeros_unicos)

outros_numeros = set()
outros_numeros.add(3)
outros_numeros.add(8)
outros_numeros.add(7)
outros_numeros.add(3)
print(outros_numeros)

outros_numeros.remove(7)
print(outros_numeros)

numeros = list(set(numeros))
print(numeros)