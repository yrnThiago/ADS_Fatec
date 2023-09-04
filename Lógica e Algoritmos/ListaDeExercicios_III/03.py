# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
# anual de crescimento de 3% e que a po
# pulação de B seja 200000 habitantes com uma taxa de
# crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
# necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento

def calcula_anos(pais_a: int, taxa_a: float, pais_b: int, taxa_b: float) -> int:
    anos = 0

    while pais_a <= pais_b:
        pais_a += pais_a * taxa_a
        pais_b += pais_b * taxa_b

        anos += 1

    return anos

print(f"{calcula_anos(80000, 0.03, 200000, 0.015)} anos")