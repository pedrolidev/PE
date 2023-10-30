import random

contador = [0, 0, 0, 0, 0, 0]

for i in range(100):
    resultado = random.randint(1, 6)

    contador[resultado - 1] += 1

for j in range(6):
    print('O número  foi emitido {i + 1}: {contagem[i] f} vezes')