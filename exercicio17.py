salario_atual = float(input("qual o seu salario atual? "))

if salario_atual <= 280:
  reajuste = salario_atual * 0.20
  novo_salario = salario_atual + reajuste
  print("seu novo salario e de ", novo_salario, "com um aumento de 20% e portanto um aumento de:",reajuste)
elif salario_atual <= 700:
  reajuste = salario_atual * 0.15
  novo_salario = salario_atual + reajuste
  print("seu novo salario e de ", novo_salario, "com um aumento de 15% e portanto um aumento de:",reajuste)
elif salario_atual <= 1500:
  reajuste = salario_atual * 0.10
  novo_salario = salario_atual + reajuste
  print("seu novo salario e de ", novo_salario, "com um aumento de 10% e portanto um aumento de:",reajuste)
else:
  reajuste = salario_atual * 0.05
  novo_salario = salario_atual + reajuste
  print("seu novo salario e de ", novo_salario, "com um aumento de 5% e portanto um aumento de:",reajuste)