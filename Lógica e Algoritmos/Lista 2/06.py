def calcula_e_mostra_salario_e_descontos(ganho_hora: float, horas_trabalhadas: int) -> str:
    salario_bruto = ganho_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - ir - inss - sindicato

    return f"""
    + Salário Bruto: R$ {salario_bruto}\n
    - IR(11%): R$ {ir}\n
    - INSS(8%): R$ {inss}\n
    - Sindicato(5%): R$ {sindicato}\n
    = Salário Liquido: R$ {salario_liquido}
    """

ganho_hora = float(input())
horas_trabalhadas = int(input())
print(calcula_e_mostra_salario_e_descontos(ganho_hora, horas_trabalhadas))