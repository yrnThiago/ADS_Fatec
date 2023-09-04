from random import randint

numeros = [randint(1, 100) for _ in range(10)]
maior, menor = 1, 100

for num in numeros:
    if num >= maior: maior = num
    if num <= menor: menor = num

print(f"{numeros}\nMaior: {maior}\nMenor: {menor}")