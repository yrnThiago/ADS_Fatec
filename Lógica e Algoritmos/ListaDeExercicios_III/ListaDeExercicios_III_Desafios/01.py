def verifica_se_num_eh_triangular(n: int) -> bool:
    cont = 1
    while True:
        tn = cont * (cont + 1) / 2
        if tn == n: return True
        elif tn > n: return False

        n += 1

    
n = int(input())
print(verifica_se_num_eh_triangular(n))
