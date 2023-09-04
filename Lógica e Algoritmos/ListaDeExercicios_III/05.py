# Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
# o algoritmo de Euclides

def mdc(numeros: list) -> int:
    maior, menor = sorted(numeros)

    while True:
        resto = maior % menor
        if not resto:
            return menor
        
        maior = menor
        menor = resto

x, y = map(int, input().split())
print(mdc([x, y]))
