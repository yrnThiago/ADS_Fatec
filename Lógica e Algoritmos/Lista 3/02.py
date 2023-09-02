# Faça um programa que leia um nome de
# usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

def credenciais_sao_validas(nome_de_usuario: str, senha: str) -> bool:
    return nome_de_usuario != senha

while True:
    nome_de_usuario = input()
    senha = input()

    if credenciais_sao_validas(nome_de_usuario, senha):
        break

    print("Senha inválida! Digite as credenciais novamente...")

