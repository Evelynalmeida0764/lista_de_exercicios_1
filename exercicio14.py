numero = input("qual o numero da sua conta? ")
saldo_atual = float(input("e qual seria seu saldo atual? "))
debito = float(input("e quais seriam os debitos para esse saldo? "))
credito = float(input("e agora quais serias os creditos? "))

saldo = saldo_atual - debito + credito

if saldo >= 0:
  print("seu saldo e positivo")
else:
  print("seu saldo e negativo")
