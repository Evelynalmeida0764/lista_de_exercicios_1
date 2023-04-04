kilometro = float(input("quantos kilometros voce usara nessa viagem? "))
litro = int(input("quantos kilometros por litro seu carro faz? "))
gasolina = float(input("qual o preco da gosolina? "))

gasto = gasolina * litro
litro = litro / kilometro
print("voce gastara $", gasto)
