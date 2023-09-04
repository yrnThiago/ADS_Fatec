from random import randint

pares, impares = [], []
numeros = [randint(1, 100) for _ in range(20)]

for num in numeros:
    if num % 2 == 0: pares.append(num)
    else: impares.append(num)

print(numeros, pares, impares)
