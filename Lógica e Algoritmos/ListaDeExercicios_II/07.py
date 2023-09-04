from math import ceil

def calcula_valor_a_pagar(latas: int) -> float:
    return latas * 80.00

def calcula_quantas_latas_sao_necessarias(area: int) -> int:
    return ceil(area / 3 / 18)

def get_qtd_latas_e_valor_total(area: int) -> tuple:
    latas = calcula_quantas_latas_sao_necessarias(area)
    valor_total = calcula_valor_a_pagar(latas)

    return latas, valor_total

area = int(input())
qtd_latas, preco_total =  get_qtd_latas_e_valor_total(area) 
print(f"Quantidade de latas: {qtd_latas} - Preço total: R$ {preco_total:.2f}")
