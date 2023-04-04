nome = input("qual seu nome? ")
idade = int(input(" quantos anos voce tem?"))

if idade <= 2:
  tipo = "bebê"
elif idade <= 11:
  tipo + "criança"
elif idade <= 21:
  tipo = "jovem"
elif idade <= 64:
  tipo = "adulto"
elif idade <= 100:
  tipo = "idoso"
else:
  tipo = "muito velinho"

print(f"Olá, {nome}! Você é um(a) {tipo}.")
  