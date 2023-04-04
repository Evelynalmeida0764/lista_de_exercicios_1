preco = float(input("quanto custou esse produto? "))

if preco < 50:
  aumento = preco * 0.45
else:
  aumento = preco * 0.30

novo_preco = preco + aumento

print("voce deve vender a $", novo_preco)