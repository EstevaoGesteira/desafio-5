senha = input("Crie uma senha: ")
tem_numero = False
tem_maiuscula = False

for caractere in senha:
    if caractere in "0123456789":
        tem_numero = True
    if caractere in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        tem_maiuscula = True

if len(senha) >= 8 and tem_numero and tem_maiuscula:
    print("Senha forte")
else:
    print("Senha fraca")
    if len(senha) < 8:
        print("- Use pelo menos 8 caracteres")
    if not tem_numero:
        print("- Inclua pelo menos um número")
    if not tem_maiuscula:
        print("- Inclua pelo menos uma letra maiúscula")