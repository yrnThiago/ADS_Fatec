def verifica_se_ano_eh_bissexto(ano: int) -> bool:
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

ano = int(input())
print(f"{ano} {'é' if verifica_se_ano_eh_bissexto(ano) else 'não é'} um ano bissexto")