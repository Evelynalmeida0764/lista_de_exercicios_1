sexo = input(" voce e Homem ou Mulher? ")
h = float(input("qual sua altura? "))

if sexo =="Homem":
  peso = 72.7*h - 58
else:
  peso = 62.1*h - 44.7

print("seu peso ideal e:", peso, "Kg")