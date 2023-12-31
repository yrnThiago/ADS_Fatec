def mostra_troco(conta_a_ser_paga: float, valor_pago: float) -> str:
    notas_troco = [50, 20, 10, 5, 2, 1]

    troco = valor_pago - conta_a_ser_paga
    troco_em_notas = f"Troco: R$ {troco:.2f}\n"
    for nota in notas_troco:
        qtd_notas = troco // nota
        troco %= nota
        troco_em_notas += f"  {qtd_notas:.0f} nota(s) de R${nota:.2f}\n"

    return troco_em_notas
        
conta_a_ser_paga, valor_pago = map(float, input().split())
print(mostra_troco(conta_a_ser_paga, valor_pago))
