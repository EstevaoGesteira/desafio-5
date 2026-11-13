quantidade = int(input("Quantas vendas? "))

total = 0
for i in range(1, quantidade + 1):
    valor = float(input(f"Venda {i}: R$ "))
    if i == 1:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    total += valor
    
print(f"Maior venda: R$ {maior:.2f}")
print(f"Menor venda: R$ {menor:.2f}")
print(f"Média: R$ {total / quantidade:.2f}")