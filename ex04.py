total = 0 # acumulador
quantidade = 0 # contador

valor = float(input("Valor da venda (0 para encerrar): R$"))
while valor != 0:
    if valor < 0:
        print("Valor inválido, venda ignorada.")
    else:
        total += valor
        quantidade += 1
    valor = float(input("Valor da venda (0 para encerrar):R$ "))

print(f"Vendas registradas: {quantidade}")
print(f"Total vendido: R$ {total:.2f}")