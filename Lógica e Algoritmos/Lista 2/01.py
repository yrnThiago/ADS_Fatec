def forma_triangulo(a: float, b: float, c: float) -> bool:
    return a >= b + c

def tipo_do_triangulo(a: float, b: float, c: float) -> str:
    if a == b == c:
        return 'EQUILATERO'
    elif a != b != c:
        return "ESCALENO"
    
    return 'ISOSCELES'
    

lado_menor, lado_medio, lado_maior = sorted(map(float, input().split(' ')))
if forma_triangulo(lado_menor, lado_medio, lado_maior):
    print(f"TRIÂNGULO {tipo_do_triangulo(lado_menor, lado_medio, lado_maior)}")
else:
    print("NÃO FORMA TRIÂNGULO")
