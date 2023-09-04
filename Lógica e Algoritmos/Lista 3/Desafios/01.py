def eh_triangular(n: int) -> bool:
    x = 1
    while x < n:
        x * (x + 1) / 2
        x += 1
    return n

n = int(input())