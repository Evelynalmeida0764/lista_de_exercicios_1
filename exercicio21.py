salario_atual = float(input("qual seu salario atual? "))
vendas = float(input("e qual foi o valor de suas vendas? "))

reajuste = salario_atual * 0.04
novo_salario = salario_atual + reajuste
print("seu novo salario e de ", novo_salario, "com um reajuste de:",reajuste)