def tem_peso_excesso(peso: int) -> bool:
    return peso > peso_max_kg

def calcula_multa_e_excesso(peso: int) -> str:
    if tem_peso_excesso(peso):
        excesso = peso - peso_max_kg
        multa = 4.0 * excesso

        return f"Excesso: {excesso}Kg - Multa: R$ {multa:.2f}"
    
    return "Excesso: ZERO - Multa: ZERO"

peso_max_kg = 50
peso = int(input())
print(calcula_multa_e_excesso(peso))
