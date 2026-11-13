SENHA_CORRETA = "python"
tentativas = 0

while tentativas < 3:
    senha = input("Senha: ")
    tentativas += 1
    if senha == SENHA_CORRETA:
        print("Acesso liberado")
        break
    print(f"Senha incorreta. Tentativas restantes: {3 -tentativas}")

if senha != SENHA_CORRETA:
    print("Conta bloqueada")