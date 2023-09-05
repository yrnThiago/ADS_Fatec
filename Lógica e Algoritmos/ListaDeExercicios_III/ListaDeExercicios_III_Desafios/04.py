def mostra_decomposicao(n: int) -> bool:
    for divisor in range(2, n):
        while n % divisor == 0:
            print(divisor)
            n /= divisor

n = int(input())
mostra_decomposicao(n)
