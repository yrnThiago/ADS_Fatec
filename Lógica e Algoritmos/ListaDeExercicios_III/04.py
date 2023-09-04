# A seqüê
# ncia de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
# soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o
# seu número
# de Fibonacci. F
# 1
# = 1, F
# 2
# = 1, F
# 3
# = 2, etc

def fib(x: int) -> int:
    ini, fim = 0, 1
    
    for _ in range(x):
        proximo_elem = ini + fim
        ini = fim
        fim = proximo_elem

    return ini

print(fib(int(input())))