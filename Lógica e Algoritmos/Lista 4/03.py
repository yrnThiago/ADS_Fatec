from random import randint

v1 = [randint(1, 100) for _ in range(10)]
v2 = [randint(1, 100) for _ in range(10)]
v3 = v1 + v2

print(v1, v2, v3)
