valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    imposto_de_renda = 0
elif salario_bruto <= 1500:
    imposto_de_renda = salario_bruto * 0.05
elif salario_bruto <= 2500:
    imposto_de_renda = salario_bruto * 0.1
else:
    imposto_de_renda = salario_bruto * 0.2

inss = salario_bruto * 0.1
total_descontos = imposto_de_renda + inss + (salario_bruto * 0.03)
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"(-) IR ({imposto_de_renda * 100 / salario_bruto:.0f}%): R$ {imposto_de_renda:.2f}")
print(f"(-) INSS ({inss*100/salario_bruto:.0f}%): R$ {inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")