# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

def nota_eh_valida(nota: float) -> bool:
    return 0 <= nota <= 10

while True:
    nota = float(input())
    if nota_eh_valida(nota):
        break
    
    print("Nota inválida! Digite novamente...")